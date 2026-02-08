#!/usr/bin/env python3
"""Enrich news content frontmatter with source and news_type fields.

Reads all content/news/*.md files, adds `source` and `news_type` fields
based on URL domain mapping and existing tags, and removes `tags` field.
Also marks meta pages (2000-dated) as draft.

Usage:
    python3 scripts/enrich_news.py [--dry-run]
"""

import os
import re
import sys
from urllib.parse import urlparse

CONTENT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "content", "news")

# URL domain -> source name mapping
DOMAIN_TO_SOURCE = {
    # International media
    "newscientist.com": "New Scientist",
    "nature.com": "Nature",
    "science.org": "Science",
    "scientificamerican.com": "Scientific American",
    "nytimes.com": "The New York Times",
    "bbc.co.uk": "BBC",
    "bbc.com": "BBC",
    "wired.com": "Wired",
    "wired.co.uk": "Wired",
    "theguardian.com": "The Guardian",
    "economist.com": "The Economist",
    "nationalgeographic.com": "National Geographic",
    "discovermagazine.com": "Discover",
    "livescience.com": "Live Science",
    "popsci.com": "Popular Science",
    "technologyreview.com": "MIT Technology Review",
    "ieee.org": "IEEE",
    "spectrum.ieee.org": "IEEE Spectrum",
    "sciencedaily.com": "ScienceDaily",
    "sciencemag.org": "Science",
    "eurekalert.org": "EurekAlert",
    "phys.org": "Phys.org",
    "thetimes.co.uk": "The Times",
    "telegraph.co.uk": "The Telegraph",
    "ft.com": "Financial Times",
    "theatlantic.com": "The Atlantic",
    "newyorker.com": "The New Yorker",
    "washingtonpost.com": "The Washington Post",
    "reuters.com": "Reuters",
    "vice.com": "VICE",
    "vox.com": "Vox",
    "cnn.com": "CNN",
    "abc.net.au": "ABC Australia",
    "smithsonianmag.com": "Smithsonian",
    "quantamagazine.org": "Quanta Magazine",
    "theconversation.com": "The Conversation",
    "sciencenode.org": "Science Node",
    "newatlas.com": "New Atlas",
    "gizmodo.com": "Gizmodo",

    # Japanese newspapers
    "asahi.com": "朝日新聞",
    "mainichi.jp": "毎日新聞",
    "nikkei.com": "日本経済新聞",
    "yomiuri.co.jp": "読売新聞",
    "sankei.com": "産経新聞",
    "kyoto-np.co.jp": "京都新聞",
    "kobe-np.co.jp": "神戸新聞",
    "47news.jp": "共同通信",
    "jiji.com": "時事通信",
    "kahoku.news": "河北新報",

    # Japanese broadcasting
    "nhk.jp": "NHK",
    "nhk.or.jp": "NHK",
    "tbs.co.jp": "TBS",
    "tv-asahi.co.jp": "テレビ朝日",
    "ntv.co.jp": "日本テレビ",
    "fujitv.co.jp": "フジテレビ",
    "mbs.jp": "MBS",
    "ytv.co.jp": "読売テレビ",

    # Japanese magazines / web media
    "nikkei-science.com": "日経サイエンス",
    "nikkeibp.co.jp": "日経BP",
    "toyokeizai.net": "東洋経済",
    "diamond.jp": "ダイヤモンド",
    "bunshun.jp": "文藝春秋",
    "gendai.media": "現代ビジネス",
    "bijutsutecho.com": "美術手帖",
    "natgeo.nikkeibp.co.jp": "ナショナルジオグラフィック日本版",
    "jst.go.jp": "JST",
    "atr.jp": "ATR",
    "i.kyoto-u.ac.jp": "Kyoto University",
    "kyoto-u.ac.jp": "Kyoto University",
    "amed.go.jp": "AMED",
    "nedo.go.jp": "NEDO",
    "riken.jp": "RIKEN",
    "itmedia.co.jp": "ITmedia",
    "impress.co.jp": "Impress",
    "gigazine.net": "GIGAZINE",
    "gakken.co.jp": "学研",
    "note.com": "note.com",
    "note.mu": "note.com",
    "vogue.co.jp": "Vogue Japan",

    # More international media
    "interestingengineering.com": "Interesting Engineering",
    "webwire.com": "WebWire",
    "tokyoartbeat.com": "Tokyo Art Beat",
    "sonar.es": "Sonar",
    "sonarplusd.com": "Sonar+D",
    "theverge.com": "The Verge",
    "engadget.com": "Engadget",
    "arstechnica.com": "Ars Technica",
    "salon.com": "Salon",

    # More Japanese media
    "j-wave.co.jp": "J-WAVE",
    "newspicks.com": "NewsPicks",
    "neurotechjp.com": "NeurotechJP",
    "medical-tribune.co.jp": "Medical Tribune",
    "newtonpress.co.jp": "Newton",
    "msz.co.jp": "みすず書房",
    "kanekoshobo.co.jp": "金子書房",
    "note.kanekoshobo.co.jp": "金子書房",
    "kyodai-original.co.jp": "京大オリジナル",
    "shitsukan.jp": "多元質感知",
    "ieice-taikai.jp": "電子情報通信学会",
    "ieice.org": "電子情報通信学会",
    "ite.or.jp": "映像情報メディア学会",
    "visionsociety.jp": "日本視覚学会",
    "jrecin.jst.go.jp": "JREC-IN",
    "newtonpress.co.jp": "Newton",
    "news.yahoo.co.jp": "Yahoo!ニュース",
    "yahoo.co.jp": "Yahoo! Japan",
    "asakura.co.jp": "朝倉書店",
    "iwanami.co.jp": "岩波書店",
    "ipsj.or.jp": "情報処理学会",
    "research-er.jp": "研究者リゾルバー",
    "sciencedirect.com": "ScienceDirect",
    "science.org": "Science",
    "annualreviews.org": "Annual Reviews",
    "doi.org": "DOI",
    "peatix.com": "Peatix",
    "vimeo.com": "Vimeo",
    "twitter.com": "Twitter",
    "x.com": "X",
    "mariangoodman.com": "Marian Goodman Gallery",
    "ringstedgalleriet.dk": "Ringsted Galleriet",
    "expo.atr.jp": "ATR",
    "ocw.u-tokyo.ac.jp": "東京大学OCW",
    "mcgill.ca": "McGill University",
    "conference.neuromatch.io": "Neuromatch",
    "unesco.org": "UNESCO",
    "osf.io": "OSF",
    "brainsci.jp": "脳科学若手の会",
    "hitachi-zaidan.org": "日立財団",
    "svrhm.com": "SVRHM",
    "conferences.nature.com": "Nature Conferences",
    "docs.google.com": "Google Forms",
    "naver.jp": "NAVER",
    "matome.naver.jp": "NAVER まとめ",
    "blogspot.com": "Blogspot",
    "mutek.jp": "MUTEK",
    "mutek.mx": "MUTEK",
    "sonar.es": "Sonar",
    "nikkeibp.co.jp": "日経BP",

    # Tech / code / academic
    "github.com": "GitHub",
    "arxiv.org": "arXiv",
    "speakerdeck.com": "SpeakerDeck",
    "slideshare.net": "SlideShare",
    "youtube.com": "YouTube",
    "youtu.be": "YouTube",
    "researchmap.jp": "researchmap",
    "scholar.google.com": "Google Scholar",
    "pubmed.ncbi.nlm.nih.gov": "PubMed",
    "jsps.go.jp": "JSPS",
    "brainliner.jp": "BrainLiner",
    "openneuro.org": "OpenNeuro",

    # Art
    "artreview.com": "ArtReview",
    "brooklynrail.org": "The Brooklyn Rail",
    "artforum.com": "Artforum",
    "frieze.com": "Frieze",
    "artnews.com": "ARTnews",
    "artnet.com": "artnet",
    "designboom.com": "designboom",
    "creativeapplications.net": "Creative Applications",
    "mutek.org": "MUTEK",
    "luma.org": "Luma",
    "serpentinegalleries.org": "Serpentine Galleries",
    "moma.org": "MoMA",
    "tate.org.uk": "Tate",

    # Podcasts
    "spotify.com": "Spotify",
    "podcasts.apple.com": "Apple Podcasts",
    "open.spotify.com": "Spotify",
}

# Title suffix patterns for source extraction: "title — source" or "title | source"
TITLE_SOURCE_PATTERNS = [
    r"[|｜]\s*(.+?)$",
    r"\s*[-–—]\s*(.+?)$",
    r"[（(](.+?)[)）]$",
]

# Known source strings that appear in titles
KNOWN_TITLE_SOURCES = {
    "朝日新聞": "朝日新聞",
    "朝日新聞デジタル": "朝日新聞",
    "毎日新聞": "毎日新聞",
    "読売新聞": "読売新聞",
    "産経新聞": "産経新聞",
    "日本経済新聞": "日本経済新聞",
    "京都新聞": "京都新聞",
    "NHK": "NHK",
    "日経サイエンス": "日経サイエンス",
    "Nature": "Nature",
    "SCIENTIFIC AMERICAN": "Scientific American",
    "BBC": "BBC",
    "New Scientist": "New Scientist",
    "Wired": "Wired",
}

# Meta pages to mark as draft (2000-dated Tumblr navigation pages)
META_PAGE_PATTERNS = [
    "2000-09-30-access-atr",
    "2000-10-20-access-ku",
    "2000-10-21-members-atr",
    "2000-10-21-members-kyoto",
    "2000-09-01-google-scholar",
    "2000-10-21-yukiyasu-kamitani-researcher",
    "2000-10-19-kamitani-yukiyasu",
    "2000-08-19-japanese-papers",
    "2000-07-19-grants-in-aid",
    "2000-10-21-神谷之康-研究者-researchmap",
    "2000-03-31-神谷之康先生",
]


def get_source_from_url(url):
    """Extract source name from URL domain."""
    if not url:
        return None
    try:
        parsed = urlparse(url)
        hostname = parsed.hostname or ""
        hostname = hostname.lower()
        if hostname.startswith("www."):
            hostname = hostname[4:]

        # Try exact match first
        if hostname in DOMAIN_TO_SOURCE:
            return DOMAIN_TO_SOURCE[hostname]

        # Try parent domain
        parts = hostname.split(".")
        for i in range(len(parts)):
            domain = ".".join(parts[i:])
            if domain in DOMAIN_TO_SOURCE:
                return DOMAIN_TO_SOURCE[domain]

        return None
    except Exception:
        return None


def get_source_from_title(title):
    """Try to extract source from title patterns."""
    for known, source in KNOWN_TITLE_SOURCES.items():
        if known in title:
            return source
    return None


def derive_news_type(tags, url, title):
    """Derive news_type from tags and URL."""
    tags_lower = [t.lower() for t in tags] if tags else []
    url_lower = (url or "").lower()

    # TV broadcasts
    if any(t in tags_lower for t in ["tv", "television"]):
        return "tv"
    if "nhk.jp" in url_lower or "nhk.or.jp" in url_lower:
        if any(kw in title for kw in ["サイエンスZERO", "サイエンスｚｅｒｏ", "ヒューマニエンス",
                                       "モーガン・フリーマン", "ドキュメンタリー", "超定義"]):
            return "tv"

    # Videos
    if any(t in tags_lower for t in ["movie", "movies", "youtube"]):
        return "video"
    if "youtube.com" in url_lower or "youtu.be" in url_lower:
        return "video"

    # Podcasts
    if any(t in tags_lower for t in ["podcast", "radio"]):
        return "podcast"

    # Awards
    if any(t in tags_lower for t in ["award", "awards"]):
        return "award"

    # Events
    if any(t in tags_lower for t in ["event", "events", "seminar", "seminars",
                                      "talk", "talks", "lecture", "lectures",
                                      "workshop", "symposium"]):
        return "event"

    # Code / data releases
    if any(t in tags_lower for t in ["sharing", "codes", "code", "github",
                                      "database", "data"]):
        return "code"
    if "github.com" in url_lower:
        return "code"
    if "arxiv.org" in url_lower:
        return "code"
    if "speakerdeck.com" in url_lower or "slideshare.net" in url_lower:
        return "presentation"

    # Books / essays
    if any(t in tags_lower for t in ["book", "books"]):
        return "book"
    if any(t in tags_lower for t in ["essay", "essays"]):
        return "essay"

    # Presentations
    if any(t in tags_lower for t in ["presentation", "presentations"]):
        return "presentation"

    # Default to media
    return "media"


def parse_frontmatter(content):
    """Parse YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return None, content

    end = content.find("---", 3)
    if end == -1:
        return None, content

    fm_text = content[3:end].strip()
    body = content[end + 3:].lstrip("\n")

    # Simple YAML parser for the fields we need
    fm = {}
    current_key = None
    current_list = None

    for line in fm_text.split("\n"):
        # Skip empty lines
        if not line.strip():
            continue

        # List item
        if line.startswith("  - ") or line.startswith("    - "):
            if current_list is not None:
                val = line.strip().lstrip("- ").strip()
                # Remove quotes
                if val.startswith('"') and val.endswith('"'):
                    val = val[1:-1]
                current_list.append(val)
            continue

        # Key: value
        match = re.match(r'^(\w+):\s*(.*)', line)
        if match:
            key = match.group(1)
            val = match.group(2).strip()

            # Remove quotes and unescape
            if val.startswith('"') and val.endswith('"'):
                val = val[1:-1].replace('\\"', '"')
            elif val.startswith("'") and val.endswith("'"):
                val = val[1:-1]

            if val == "" or val == "[]":
                # Could be a list starting on next line
                fm[key] = []
                current_key = key
                current_list = fm[key]
            else:
                # Handle inline list: ["tag1", "tag2"]
                if val.startswith("[") and val.endswith("]"):
                    items = val[1:-1]
                    parsed_items = []
                    for item in re.findall(r'"([^"]*)"', items):
                        parsed_items.append(item)
                    fm[key] = parsed_items
                    current_list = None
                else:
                    fm[key] = val
                    current_list = None
                current_key = key

    return fm, body


def rebuild_frontmatter(fm, body):
    """Rebuild markdown file from frontmatter dict and body."""
    lines = ["---"]

    # Write fields in a consistent order
    field_order = ["title", "date", "source", "news_type", "link_url", "tumblr_url", "draft"]

    for key in field_order:
        if key in fm:
            val = fm[key]
            if isinstance(val, list):
                if val:
                    lines.append(f"{key}:")
                    for item in val:
                        lines.append(f'  - "{item}"')
                else:
                    lines.append(f"{key}: []")
            elif isinstance(val, bool):
                lines.append(f"{key}: {'true' if val else 'false'}")
            elif key in ("title", "source", "link_url", "tumblr_url"):
                # Always quote strings that may contain special chars
                escaped = val.replace('"', '\\"')
                lines.append(f'{key}: "{escaped}"')
            else:
                lines.append(f"{key}: {val}")

    # Write any remaining keys not in field_order
    for key, val in fm.items():
        if key in field_order or key == "tags":
            continue
        if isinstance(val, list):
            if val:
                lines.append(f"{key}:")
                for item in val:
                    lines.append(f'  - "{item}"')
        elif isinstance(val, bool):
            lines.append(f"{key}: {'true' if val else 'false'}")
        else:
            escaped = str(val).replace('"', '\\"')
            lines.append(f'{key}: "{escaped}"')

    lines.append("---")
    return "\n".join(lines) + "\n" + body


def is_meta_page(filename):
    """Check if this is a meta page that should be drafted."""
    for pattern in META_PAGE_PATTERNS:
        if pattern in filename:
            return True
    return False


def process_file(filepath, dry_run=False):
    """Process a single news markdown file. Returns (changed, result_fm)."""
    filename = os.path.basename(filepath)

    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    fm, body = parse_frontmatter(content)
    if fm is None:
        print(f"  SKIP (no frontmatter): {filename}")
        return False, {}

    changed = False

    # Mark meta pages as draft
    if is_meta_page(filename):
        if fm.get("draft") != "true":
            fm["draft"] = "true"
            changed = True
            print(f"  DRAFT: {filename}")

    # Derive source
    if "source" not in fm:
        link_url = fm.get("link_url", "")
        title = fm.get("title", "")

        source = get_source_from_url(link_url)
        if not source:
            source = get_source_from_title(title)

        if source:
            fm["source"] = source
            changed = True

    # Derive news_type
    if "news_type" not in fm:
        tags = fm.get("tags", [])
        link_url = fm.get("link_url", "")
        title = fm.get("title", "")

        news_type = derive_news_type(tags, link_url, title)
        fm["news_type"] = news_type
        changed = True

    # Remove tags
    if "tags" in fm:
        del fm["tags"]
        changed = True

    if changed and not dry_run:
        new_content = rebuild_frontmatter(fm, body)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)

    return changed, fm


def main():
    dry_run = "--dry-run" in sys.argv

    if dry_run:
        print("DRY RUN - no files will be modified\n")

    files = sorted([f for f in os.listdir(CONTENT_DIR)
                    if f.endswith(".md") and not f.startswith("_")])

    print(f"Processing {len(files)} news files...\n")

    stats = {
        "total": len(files),
        "modified": 0,
        "with_source": 0,
        "without_source": 0,
        "drafted": 0,
        "types": {},
    }

    for filename in files:
        filepath = os.path.join(CONTENT_DIR, filename)
        changed, fm = process_file(filepath, dry_run)
        if changed:
            stats["modified"] += 1

        if fm:
            if fm.get("source"):
                stats["with_source"] += 1
            else:
                stats["without_source"] += 1
                print(f"  NO SOURCE: {filename} -> {fm.get('link_url', 'no url')}")

            news_type = fm.get("news_type", "unknown")
            stats["types"][news_type] = stats["types"].get(news_type, 0) + 1

            if fm.get("draft") == "true":
                stats["drafted"] += 1

    print(f"\n{'='*60}")
    print(f"Total files: {stats['total']}")
    print(f"Modified: {stats['modified']}")
    print(f"With source: {stats['with_source']}")
    print(f"Without source: {stats['without_source']}")
    print(f"Drafted (meta pages): {stats['drafted']}")
    print(f"\nType breakdown:")
    for t, c in sorted(stats["types"].items(), key=lambda x: -x[1]):
        print(f"  {t}: {c}")


if __name__ == "__main__":
    main()
