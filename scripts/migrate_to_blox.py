#!/usr/bin/env python3
"""Migrate Kamitani Lab content from Ananke to Hugo Blox structure.

Converts:
  - content/papers/ → content/publication/<slug>/index.md (page bundles)
  - content/news/  → content/post/<filename>.md (flat files)
  - content/art/   → content/project/<filename>.md (flat files)
  - data/members.yaml → content/authors/<slug>/_index.md
"""

import os
import re
import shutil
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def parse_frontmatter(filepath):
    """Parse YAML frontmatter and body from a markdown file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.startswith("---"):
        return {}, content

    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content

    fm = yaml.safe_load(parts[1]) or {}
    body = parts[2].lstrip("\n")
    return fm, body


def write_frontmatter(filepath, fm, body):
    """Write YAML frontmatter and body to a markdown file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(yaml.dump(fm, allow_unicode=True, default_flow_style=False, sort_keys=False))
        f.write("---\n")
        if body:
            f.write("\n" + body)


def slug_from_filename(filename):
    """Extract slug from a filename like '2005-04-24-paper-decoding-the-visual.md'."""
    name = os.path.splitext(filename)[0]
    # Remove date prefix (YYYY-MM-DD-)
    match = re.match(r"\d{4}-\d{2}-\d{2}-(.*)", name)
    if match:
        return match.group(1)
    return name


def migrate_papers():
    """Migrate content/papers/ → content/publication/ as page bundles."""
    src_dir = os.path.join(ROOT, "content", "papers")
    dst_dir = os.path.join(ROOT, "content", "publication")
    os.makedirs(dst_dir, exist_ok=True)

    # First pass: detect duplicate slugs
    files = sorted(f for f in os.listdir(src_dir) if not f.startswith("_index") and f.endswith(".md"))
    slug_counts = {}
    for filename in files:
        slug = slug_from_filename(filename)
        slug_counts[slug] = slug_counts.get(slug, 0) + 1

    count = 0
    for filename in files:
        filepath = os.path.join(src_dir, filename)
        fm, body = parse_frontmatter(filepath)

        base_slug = slug_from_filename(filename)

        # If duplicate slug, prepend date to make unique
        if slug_counts[base_slug] > 1:
            date_prefix = os.path.splitext(filename)[0][:10]  # YYYY-MM-DD
            slug = f"{date_prefix}-{base_slug}"
        else:
            slug = base_slug

        # Clean title: remove [paper] prefix
        title = fm.get("title", "")
        title = re.sub(r"^\[paper\]\s*", "", title, flags=re.IGNORECASE)
        fm["title"] = title

        # Convert link_url to links array
        link_url = fm.pop("link_url", None)
        if link_url:
            fm["links"] = [{"name": "Paper", "url": link_url}]

        # Add publication_types and featured
        fm["publication_types"] = ["article-journal"]
        fm["featured"] = False

        # Add alias for old URL redirect
        fm["aliases"] = [f"/papers/{base_slug}/"]

        # Remove draft if false
        if fm.get("draft") is False:
            del fm["draft"]

        # Write as page bundle
        bundle_dir = os.path.join(dst_dir, slug)
        os.makedirs(bundle_dir, exist_ok=True)
        write_frontmatter(os.path.join(bundle_dir, "index.md"), fm, body)
        count += 1

    print(f"  Migrated {count} papers → publication/")


def migrate_news():
    """Migrate content/news/ → content/post/ as flat files."""
    src_dir = os.path.join(ROOT, "content", "news")
    dst_dir = os.path.join(ROOT, "content", "post")
    os.makedirs(dst_dir, exist_ok=True)

    count = 0
    for filename in sorted(os.listdir(src_dir)):
        if filename.startswith("_index"):
            continue
        if not filename.endswith(".md"):
            continue

        filepath = os.path.join(src_dir, filename)
        fm, body = parse_frontmatter(filepath)

        slug = slug_from_filename(filename)

        # Convert link_url to links array
        link_url = fm.pop("link_url", None)
        if link_url:
            fm["links"] = [{"name": "Link", "url": link_url}]

        # Add alias for old URL redirect
        fm["aliases"] = [f"/news/{slug}/"]

        # Remove draft if false
        if fm.get("draft") is False:
            del fm["draft"]

        write_frontmatter(os.path.join(dst_dir, filename), fm, body)
        count += 1

    print(f"  Migrated {count} news → post/")


def migrate_art():
    """Migrate content/art/ → content/project/ as flat files."""
    src_dir = os.path.join(ROOT, "content", "art")
    dst_dir = os.path.join(ROOT, "content", "project")
    os.makedirs(dst_dir, exist_ok=True)

    count = 0
    for filename in sorted(os.listdir(src_dir)):
        if filename.startswith("_index"):
            continue
        if not filename.endswith(".md"):
            continue

        filepath = os.path.join(src_dir, filename)
        fm, body = parse_frontmatter(filepath)

        slug = slug_from_filename(filename)

        # Convert link_url to links array
        link_url = fm.pop("link_url", None)
        if link_url:
            fm["links"] = [{"name": "Link", "url": link_url}]

        # Add alias for old URL redirect
        fm["aliases"] = [f"/art/{slug}/"]

        # Remove draft if false
        if fm.get("draft") is False:
            del fm["draft"]

        write_frontmatter(os.path.join(dst_dir, filename), fm, body)
        count += 1

    print(f"  Migrated {count} art → project/")


def make_slug(name):
    """Create a URL-safe slug from a name."""
    slug = name.lower().strip()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = slug.strip("-")
    return slug


def migrate_members():
    """Migrate data/members.yaml → content/authors/."""
    yaml_path = os.path.join(ROOT, "data", "members.yaml")
    authors_dir = os.path.join(ROOT, "content", "authors")
    os.makedirs(authors_dir, exist_ok=True)

    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    # Collect all members, merging duplicates (e.g., Kamitani appears in staff + atr_staff)
    members = {}  # slug -> member data

    def process_member(member, section):
        slug = make_slug(member["name"])
        if slug not in members:
            members[slug] = {
                "name": member["name"],
                "name_ja": member.get("name_ja", ""),
                "roles": [],
                "role_ja_list": [],
                "user_groups": [],
                "links": [],
                "affiliations": [],
                "levels": [],
            }

        m = members[slug]

        role = member.get("role", member.get("level", ""))
        role_ja = member.get("role_ja", "")

        if role and role not in m["roles"]:
            m["roles"].append(role)
        if role_ja and role_ja not in m["role_ja_list"]:
            m["role_ja_list"].append(role_ja)

        # Map section to user_groups
        if section == "staff":
            if role == "Professor":
                groups = ["Principal Investigators", "Kyoto University"]
            else:
                groups = ["Researchers", "Kyoto University"]
        elif section == "students":
            groups = ["Grad Students", "Kyoto University"]
        elif section == "atr_staff":
            groups = ["ATR Researchers", "ATR"]
        elif section == "atr_students":
            groups = ["ATR Students", "ATR"]
        elif section == "atr_secretary":
            groups = ["Administration", "ATR"]
        else:
            groups = []

        for g in groups:
            if g not in m["user_groups"]:
                m["user_groups"].append(g)

        # Links
        for link in member.get("links", []):
            if link not in m["links"]:
                m["links"].append(link)

        # Affiliation
        aff = member.get("affiliation", "")
        if aff and aff not in m["affiliations"]:
            m["affiliations"].append(aff)

        # Level (for students)
        level = member.get("level", "")
        if level and level not in m["levels"]:
            m["levels"].append(level)

    # Process all sections
    for member in data.get("staff", []):
        process_member(member, "staff")
    for member in data.get("atr_staff", []):
        process_member(member, "atr_staff")
    for member in data.get("students", []):
        process_member(member, "students")
    for member in data.get("atr_students", []):
        process_member(member, "atr_students")
    for member in data.get("atr_secretary", []):
        process_member(member, "atr_secretary")

    # Write each member as content/authors/<slug>/_index.md
    count = 0
    for slug, m in members.items():
        fm = {
            "title": m["name"],
            "role": ", ".join(m["roles"]),
            "user_groups": m["user_groups"],
        }

        # Add social/links
        social = []
        for link in m["links"]:
            social.append({
                "icon": "link",
                "icon_pack": "fas",
                "name": link.get("label", "Link"),
                "link": link.get("url", ""),
            })
        if social:
            fm["social"] = social

        # Build body with Japanese info
        body_parts = []
        if m["name_ja"]:
            body_parts.append(m["name_ja"])
        if m["role_ja_list"]:
            body_parts.append(" / ".join(m["role_ja_list"]))
        if m["affiliations"]:
            body_parts.append(", ".join(m["affiliations"]))
        if m["levels"]:
            body_parts.append(", ".join(m["levels"]))

        body = "\n\n".join(body_parts) + "\n" if body_parts else ""

        author_dir = os.path.join(authors_dir, slug)
        os.makedirs(author_dir, exist_ok=True)
        write_frontmatter(os.path.join(author_dir, "_index.md"), fm, body)
        count += 1

    print(f"  Migrated {count} members → authors/")


def main():
    print("Migrating Kamitani Lab content to Hugo Blox structure...")
    print()

    print("1. Papers → Publications")
    migrate_papers()

    print("2. News → Posts")
    migrate_news()

    print("3. Art → Projects")
    migrate_art()

    print("4. Members → Authors")
    migrate_members()

    print()
    print("Migration complete!")


if __name__ == "__main__":
    main()
