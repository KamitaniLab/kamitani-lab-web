# AGENTS.md

This file provides guidance to Codex (Codex.ai/code) when working with code in this repository.

## Project Overview

Kamitani Lab (Kyoto University & ATR) website, built with Hugo and deployed to GitHub Pages.

## Commands

```bash
# Local development server (with drafts)
hugo server --buildDrafts

# Production build + search index
hugo --gc --minify && npx pagefind --site public

# Create new content
hugo new content publications/YYYY-slug.md
hugo new content news/YYYY-MM-title.md
hugo new content art/YYYY-MM-title.md
```

Build output goes to `public/` (gitignored). Deployment is automated via GitHub Actions on push to `main` (builds Hugo, runs Pagefind, deploys).

## Architecture

- **Hugo static site** with Ananke theme (git submodule in `themes/ananke`, Tachyons CSS)
- **Bilingual** (English default, Japanese): configured in `hugo.yaml` under `languages`. Japanese pages exist only for Homepage, About, and Research.
- **GitHub Actions** deploys on push to main (`.github/workflows/deploy.yml`): checks out submodules, builds with Hugo extended, runs Pagefind, deploys to GitHub Pages.
- **Pagefind** provides static full-text search (`/search/`)

### Deployment — push to BOTH remotes

The official site (https://kamitani-lab.ist.i.kyoto-u.ac.jp) is served by the **`kamitanilab`** remote's (`KamitaniLab/kamitani-lab-web`) GitHub Pages. `origin` (`ykamit/...`) is only a personal mirror. **Pushing only to `origin` does NOT update the official site** — always push to both: `git push kamitanilab main && git push origin main`.

### Navigation

About → People → Research → Publications → Art → News → Search

### Content structure

| Directory | Purpose | Format |
|---|---|---|
| `content/publications/` | Publications (~130) | Markdown with frontmatter (authors, journal, doi, etc.) |
| `content/news/` | News, media coverage, awards (~265) | Markdown with `link_url`, `source`, `news_type` |
| `content/art/` | Art projects and collaborations (~20) | Markdown with `artist`, `venue`, `exhibitions`, etc. |
| `content/research/` | Research overview (4 areas) | Single page, `layout: "research"` |
| `content/members/` | Members listing (Kyoto U + ATR) | Shortcodes rendering `data/members.yaml` |
| `content/about/` | Lab info, affiliation, access, resources | Single page |
| `content/search/` | Search page | Pagefind UI widget |

### Custom layouts

- `layouts/publications/list.html` — Year-grouped listing with year-nav anchors
- `layouts/publications/single.html` — Paper detail page
- `layouts/news/list.html` — Year-grouped news listing
- `layouts/art/list.html` — Year-grouped art listing
- `layouts/research/research.html` — Research overview with embedded media
- `layouts/search/list.html` — Pagefind search UI
- `layouts/shortcodes/members-{staff,students,atr}.html` — Render from `data/members.yaml`

### Data files

- **`data/members.yaml`** — Staff/students for both Kyoto University and ATR labs.

### Key conventions

- External links use `link_url` (not `url`, reserved by Hugo).
- Navigation menu defined centrally in `hugo.yaml` under `menus.main`.
- Content filenames: `publications/` use `YYYY-slug.md` (no month/day); `news/` and `art/` use `YYYY-MM-DD-slug.md`.
- Section list templates group posts by year in reverse chronological order.
- Research page is a static summary (Brain Decoding, NeuroAI, BMI, Art), not a post list.
