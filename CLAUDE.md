# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Kamitani Lab (Kyoto University & ATR) website, built with Hugo and Hugo Blox (Research Group theme), deployed to GitHub Pages. Migrated from a Tumblr-based site (371 posts).

## Commands

```bash
# Local development server (with drafts)
hugo server --buildDrafts

# Production build + search index
hugo --gc --minify && npx pagefind --site public

# Update Hugo modules
hugo mod get -u && hugo mod tidy

# Create new content
hugo new content publication/YYYY-slug/index.md
hugo new content post/YYYY-MM-title.md
hugo new content project/YYYY-MM-title.md
```

Build output goes to `public/` (gitignored). Deployment is automated via GitHub Actions on push to `main` (builds Hugo, runs Pagefind, deploys).

## Architecture

- **Hugo static site** with Hugo Blox (blox-bootstrap/v5 module)
- **Bilingual** (English default, Japanese): configured in `config/_default/languages.yaml`
- **GitHub Actions** deploys on push to main (`.github/workflows/deploy.yml`)
- **Pagefind** provides static full-text search (`/search/`)

### Navigation

About → Members → Research → Publications → Artworks → News → Links → Search

### Configuration

Split configuration in `config/_default/`:

| File | Purpose |
|---|---|
| `hugo.yaml` | Core settings, module imports, permalinks, outputs |
| `params.yaml` | Theme appearance, header, footer, search, SEO |
| `menus.yaml` | English navigation menu |
| `languages.yaml` | Language settings (en/ja) with Japanese menu |

### Content structure

| Directory | Purpose | Format |
|---|---|---|
| `content/publication/` | Publications (65) | Page bundles (`<slug>/index.md`) with `publication_types`, `links` |
| `content/post/` | News, media coverage, awards (269) | Flat markdown with `links`, `external_link` |
| `content/project/` | Art projects and collaborations (36) | Flat markdown with `links`, `external_link` |
| `content/authors/` | Lab members (26) | Page bundles (`<slug>/_index.md`) with `user_groups` |
| `content/people/` | Members listing page | Landing page with `people` blocks |
| `content/research/` | Static summary page (4 areas) | Landing page with `markdown` block |
| `content/about/` | Lab info, affiliation, access | Landing page with `markdown` block |
| `content/links/` | External resources and profiles | Single page |
| `content/search/` | Search page | Custom layout (`page/search`) with Pagefind UI |

### Custom layouts

- `layouts/page/search.html` — Pagefind search UI widget

### Data files

- **`data/members.yaml`** — Original member data (reference copy; authors are in `content/authors/`)

### Key conventions

- Migrated posts use `links` array (Hugo Blox format) and `external_link` for external URLs.
- `tumblr_url` in frontmatter preserves original Tumblr post URLs.
- `aliases` in frontmatter provide redirects from old URLs (`/papers/`, `/news/`, `/art/`).
- Navigation menu defined in `config/_default/menus.yaml` (EN) and `config/_default/languages.yaml` (JA).
- Homepage and section pages use Hugo Blox `landing` type with widget `sections`.
- Members use Hugo Blox Authors system with `user_groups` for People widget grouping.
- Publications use page bundles; posts and projects use flat files.

### URL mapping (old → new)

| Old | New |
|---|---|
| `/papers/` | `/publication/` |
| `/news/` | `/post/` |
| `/art/` | `/project/` |
| `/members/` | `/people/` |

### Migration scripts

- `scripts/migrate_tumblr.py` — Fetches posts from Tumblr API, writes Hugo content files
- `scripts/migrate_to_blox.py` — Converts Ananke content to Hugo Blox structure (papers→publication, news→post, art→project, members→authors)
