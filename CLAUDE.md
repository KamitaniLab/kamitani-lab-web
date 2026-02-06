# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Kamitani Lab (Kyoto University & ATR) website, built with Hugo and deployed to GitHub Pages. Migrated from a Tumblr-based site (371 posts).

## Commands

```bash
# Local development server (with drafts)
hugo server --buildDrafts

# Production build + search index
hugo --gc --minify && npx pagefind --site public

# Create new content
hugo new content papers/YYYY-slug.md
hugo new content news/YYYY-MM-title.md
hugo new content art/YYYY-MM-title.md

# Re-run Tumblr migration (fetches all 371 posts)
python3 scripts/migrate_tumblr.py
```

Build output goes to `public/` (gitignored). Deployment is automated via GitHub Actions on push to `main` (builds Hugo, runs Pagefind, deploys).

## Architecture

- **Hugo static site** with Ananke theme (git submodule in `themes/ananke`, Tachyons CSS)
- **Bilingual** (English default, Japanese): configured in `hugo.yaml` under `languages`
- **GitHub Actions** deploys on push to main (`.github/workflows/deploy.yml`)
- **Pagefind** provides static full-text search (`/search/`)

### Navigation

About → Members → Research → Papers → Artworks → News → Links → Search

### Content structure

| Directory | Purpose | Format |
|---|---|---|
| `content/papers/` | Publications (65) | Markdown with `link_url`, `tags` |
| `content/news/` | News, media coverage, awards (270) | Markdown with `link_url`, `tags` |
| `content/art/` | Art projects and collaborations (36) | Markdown with `link_url`, `tags` |
| `content/research/` | Static summary page (4 areas) | Single page, `layout: "research"` |
| `content/members/` | Members listing (Kyoto U + ATR) | Shortcodes rendering `data/members.yaml` |
| `content/about/` | Lab info, affiliation, access | Single page |
| `content/links/` | External resources and profiles | Single page |
| `content/search/` | Search page | Pagefind UI widget |

### Custom layouts

- `layouts/papers/list.html` — Year-grouped listing with year-nav anchors
- `layouts/papers/single.html` — Paper detail with "Read paper" button
- `layouts/{news,art}/list.html` — Year-grouped card listings via `_partials/link-card.html`
- `layouts/research/research.html` — Static summary (no post list)
- `layouts/search/list.html` — Pagefind search UI
- `layouts/shortcodes/members-{staff,students,atr}.html` — Render from `data/members.yaml`

### Data files

- **`data/members.yaml`** — Staff/students for both Kyoto University and ATR labs. Sections: `staff`, `students`, `atr_staff`, `atr_students`, `atr_secretary`.

### Key conventions

- Migrated posts use `link_url` (not `url`, reserved by Hugo) for external links.
- `tumblr_url` in frontmatter preserves original Tumblr post URLs.
- Navigation menu defined centrally in `hugo.yaml` under `menus.main`.
- Content filenames follow `YYYY-MM-DD-slug.md` pattern.
- Section list templates group posts by year in reverse chronological order.
- Research page is a static summary (Brain Decoding, NeuroAI, BMI, Art), not a post list.

### Migration script

`scripts/migrate_tumblr.py` fetches all posts from the Tumblr API (`/api/read/json`), handles `regular` (NPF), `link`, and `photo` post types, classifies by tags (`papers` → papers, `art` → art, default → news), and writes Hugo Markdown files.
