#!/usr/bin/env python3
"""
Download Tumblr CDN images to static/images/posts/ and update
Markdown files to use local paths.

Usage:
    python scripts/localize_images.py
"""

import hashlib
import os
import re
import urllib.request
import urllib.error
from pathlib import Path

CONTENT_DIR = Path(__file__).resolve().parent.parent / "content"
IMAGES_DIR = Path(__file__).resolve().parent.parent / "static" / "images" / "posts"
LOCAL_PREFIX = "/images/posts"

# Match Tumblr CDN URLs
TUMBLR_URL_RE = re.compile(
    r'(https?://\d+\.media\.tumblr\.com/[^\s\)\]"\']+)'
)


def url_to_filename(url):
    """Generate a stable filename from a URL, preserving extension."""
    # Extract extension from URL
    path = url.split("?")[0]
    ext = os.path.splitext(path)[1]
    if ext not in (".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"):
        ext = ".jpg"  # default fallback
    # Use hash for unique, safe filename
    url_hash = hashlib.md5(url.encode()).hexdigest()[:12]
    # Also grab a human-readable slug from the URL
    parts = path.rstrip("/").split("/")
    slug = parts[-1] if parts else "image"
    # Sanitize slug
    slug = re.sub(r'[^\w\-.]', '_', slug)
    if len(slug) > 60:
        slug = slug[:60]
    return f"{url_hash}_{slug}"


def download_image(url, dest_path):
    """Download an image, return True on success."""
    if dest_path.exists():
        return True  # already downloaded
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read()
        dest_path.write_bytes(data)
        return True
    except (urllib.error.URLError, OSError, TimeoutError) as e:
        print(f"    FAILED: {url} ({e})")
        return False


def process_file(md_path):
    """Find Tumblr URLs in a file, download images, replace URLs."""
    text = md_path.read_text(encoding="utf-8")
    urls = TUMBLR_URL_RE.findall(text)

    if not urls:
        return 0

    count = 0
    for url in set(urls):
        filename = url_to_filename(url)
        dest = IMAGES_DIR / filename

        if download_image(url, dest):
            local_path = f"{LOCAL_PREFIX}/{filename}"
            text = text.replace(url, local_path)
            count += 1

    md_path.write_text(text, encoding="utf-8")
    return count


def main():
    print("=== Localize Tumblr Images ===\n")

    IMAGES_DIR.mkdir(parents=True, exist_ok=True)

    total_files = 0
    total_images = 0

    for md_path in sorted(CONTENT_DIR.rglob("*.md")):
        count = process_file(md_path)
        if count > 0:
            total_files += 1
            total_images += count
            print(f"  {md_path.relative_to(CONTENT_DIR)}: {count} image(s)")

    print(f"\nDone: {total_images} images downloaded across {total_files} files.")
    print(f"Images saved to: {IMAGES_DIR.relative_to(IMAGES_DIR.parent.parent.parent)}")


if __name__ == "__main__":
    main()
