#!/usr/bin/env python3
"""
Migrate Kamitani Lab Tumblr posts to Hugo Markdown files.

Usage:
    python scripts/migrate_tumblr.py

Fetches all posts from the Tumblr API and writes Hugo-compatible
Markdown files into content/ subdirectories based on tags.
"""

import json
import os
import re
import html
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path

TUMBLR_API = "https://kamitani-lab.ist.i.kyoto-u.ac.jp/api/read/json"
BATCH_SIZE = 50
CONTENT_DIR = Path(__file__).resolve().parent.parent / "content"
IMAGES_DIR = Path(__file__).resolve().parent.parent / "static" / "images" / "posts"

# Tag-to-section mapping. First matching rule wins.
# Tags are compared case-insensitively.
SECTION_RULES = [
    ({"paper", "papers"},           "papers"),
    ({"art"},                       "art"),
    # "media" and "research" tagged posts go to news (default)
]
DEFAULT_SECTION = "news"


def fetch_all_posts():
    """Fetch all posts from Tumblr API v1 (read/json)."""
    all_posts = []
    start = 0
    total = None

    while True:
        url = f"{TUMBLR_API}?num={BATCH_SIZE}&start={start}"
        print(f"  Fetching posts {start}–{start + BATCH_SIZE}...")
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                raw = resp.read().decode("utf-8")
        except urllib.error.URLError as e:
            print(f"  Error fetching {url}: {e}")
            break

        # Tumblr v1 JSON wraps in: var tumblr_api_read = {...};
        raw = raw.strip()
        if raw.startswith("var tumblr_api_read"):
            raw = raw.split("=", 1)[1].strip().rstrip(";")

        data = json.loads(raw)

        if total is None:
            total = data.get("posts-total", 0)
            print(f"  Total posts: {total}")

        posts = data.get("posts", [])
        if not posts:
            break

        all_posts.extend(posts)
        start += BATCH_SIZE

        if start >= total:
            break

    return all_posts


def classify_post(tags):
    """Determine which content section a post belongs to based on tags."""
    tag_set = {t.lower() for t in tags}
    for rule_tags, section in SECTION_RULES:
        if tag_set & rule_tags:
            return section
    return DEFAULT_SECTION


def extract_npf_link(body_html):
    """Extract link URL and title from npf_link data attribute."""
    match = re.search(r'data-npf=\'({.*?})\'', body_html)
    if match:
        try:
            npf = json.loads(match.group(1))
            return npf.get("url", ""), npf.get("title", "")
        except json.JSONDecodeError:
            pass
    # Fallback: extract first <a> href
    a_match = re.search(r'href="([^"]+)"', body_html)
    title_match = re.search(r'>([^<]+)</a>', body_html)
    link = a_match.group(1) if a_match else ""
    title = title_match.group(1) if title_match else ""
    return link, title


def extract_images(body_html):
    """Extract image URLs from post HTML."""
    return re.findall(r'<img[^>]+src="([^"]+)"', body_html)


def html_to_text(body_html):
    """Simple HTML-to-Markdown conversion for post bodies."""
    text = body_html

    # Remove npf_link blocks (we handle these separately)
    text = re.sub(r'<p class="npf_link"[^>]*>.*?</p>', '', text, flags=re.DOTALL)

    # Convert common HTML to markdown
    text = re.sub(r'<br\s*/?>', '\n', text)
    text = re.sub(r'<p[^>]*>', '\n', text)
    text = re.sub(r'</p>', '\n', text)
    text = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', text)
    text = re.sub(r'<strong>(.*?)</strong>', r'**\1**', text)
    text = re.sub(r'<em>(.*?)</em>', r'*\1*', text)
    text = re.sub(r'<blockquote[^>]*>(.*?)</blockquote>', r'> \1', text, flags=re.DOTALL)

    # Strip remaining tags
    text = re.sub(r'<[^>]+>', '', text)

    # Clean up entities
    text = html.unescape(text)

    # Clean up whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def make_slug(post):
    """Generate a filename slug from a post."""
    slug = post.get("slug", "")
    if not slug:
        slug = str(post.get("id", "unknown"))
    # Sanitize
    slug = re.sub(r'[^\w\-]', '-', slug)
    slug = re.sub(r'-+', '-', slug).strip('-')
    # Truncate long slugs
    if len(slug) > 80:
        slug = slug[:80].rstrip('-')
    return slug


def post_to_markdown(post):
    """Convert a single Tumblr post to Hugo Markdown content."""
    post_type = post.get("type", "regular")
    tags = post.get("tags", [])
    date_str = post.get("date-gmt", "")
    post_url = post.get("url-with-slug", post.get("url", ""))

    # Parse date
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S %Z")
        date_iso = dt.strftime("%Y-%m-%d")
    except (ValueError, TypeError):
        date_iso = "2020-01-01"

    link_url = ""
    link_title = ""
    body_md = ""
    images = []
    title = ""

    if post_type == "link":
        # Link-type posts (older Tumblr format)
        link_url = post.get("link-url", "")
        link_title = post.get("link-text", "")
        desc_html = post.get("link-description", "")
        if desc_html:
            body_md = html_to_text(desc_html)
            images = extract_images(desc_html)
        title = link_title

    elif post_type == "photo":
        # Photo-type posts
        caption = post.get("photo-caption", "")
        body_md = html_to_text(caption) if caption else ""
        # Collect photo URLs (Tumblr provides multiple sizes)
        photo_url = post.get("photo-url-1280", post.get("photo-url-500", ""))
        if photo_url:
            images = [photo_url]
        images.extend(extract_images(caption) if caption else [])
        title = body_md.split('\n')[0][:120] if body_md else ""

    else:
        # Regular (text) posts — includes NPF format
        body = post.get("regular-body", "")
        title_raw = post.get("regular-title", "")

        # Extract link info from npf data
        link_url, link_title = extract_npf_link(body)
        body_md = html_to_text(body)
        images = extract_images(body)

        if title_raw:
            title = title_raw.strip()
        elif link_title:
            title = link_title.strip()
        else:
            title = body_md.split('\n')[0][:120] if body_md else ""

    # Final fallback title
    if not title:
        title = f"Post {post.get('id', '')}"

    # Escape quotes in title for YAML
    title = title.replace('"', '\\"')

    # Build frontmatter
    section = classify_post(tags)
    fm_lines = [
        '---',
        f'title: "{title}"',
        f'date: {date_iso}',
    ]
    if tags:
        tags_yaml = json.dumps(tags, ensure_ascii=False)
        fm_lines.append(f'tags: {tags_yaml}')
    if link_url:
        fm_lines.append(f'link_url: "{link_url}"')
    fm_lines.append(f'tumblr_url: "{post_url}"')
    fm_lines.append('draft: false')
    fm_lines.append('---')

    # Build body
    parts = []
    if link_url:
        display = link_title if link_title else link_url
        parts.append(f'[{display}]({link_url})')
        parts.append('')
    if body_md:
        parts.append(body_md)
    if images:
        parts.append('')
        for img in images:
            parts.append(f'![image]({img})')

    content = '\n'.join(fm_lines) + '\n\n' + '\n'.join(parts) + '\n'
    return section, content


def write_post(section, slug, date_iso, content):
    """Write a markdown file to the appropriate content directory."""
    section_dir = CONTENT_DIR / section
    section_dir.mkdir(parents=True, exist_ok=True)

    filename = f"{date_iso}-{slug}.md"
    filepath = section_dir / filename

    # Handle duplicates
    counter = 1
    while filepath.exists():
        filename = f"{date_iso}-{slug}-{counter}.md"
        filepath = section_dir / filename
        counter += 1

    filepath.write_text(content, encoding="utf-8")
    return filepath


def main():
    print("=== Kamitani Lab Tumblr → Hugo Migration ===\n")

    print("[1/3] Fetching posts from Tumblr API...")
    posts = fetch_all_posts()
    print(f"  Fetched {len(posts)} posts.\n")

    if not posts:
        print("No posts found. Exiting.")
        return

    print("[2/3] Converting and writing Markdown files...")
    stats = {}
    for post in posts:
        section, content = post_to_markdown(post)
        slug = make_slug(post)

        date_str = post.get("date-gmt", "")
        try:
            dt = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S %Z")
            date_iso = dt.strftime("%Y-%m-%d")
        except (ValueError, TypeError):
            date_iso = "2020-01-01"

        filepath = write_post(section, slug, date_iso, content)
        stats[section] = stats.get(section, 0) + 1

    print(f"\n[3/3] Migration complete!\n")
    print("  Posts by section:")
    for section, count in sorted(stats.items()):
        print(f"    {section}: {count}")
    print(f"    total: {sum(stats.values())}")


if __name__ == "__main__":
    main()
