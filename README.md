# amannj.github.io

Source for [amannj.github.io](https://amannj.github.io), built with [Quarto](https://quarto.org/).

## Structure

- `index.qmd` — homepage / bio
- `research.qmd` — publications, split into Academic Publications, Working Papers, and Policy, with a client-side filter
- `news/` — short posts (new publications, code releases, occasional notes); `news.qmd` is the listing page, filterable by category
- `code.qmd` — R/Python packages
- `theme.scss` — site theme (colours, type, component styles)
- `_quarto.yml` — site configuration (navigation, theme, deployment)
- `scripts/diff_citations.py` — diffs a new Google Scholar citation export against `scripts/citations-baseline.csv` to flag what's new or changed before updating `research.qmd` by hand

## Local development

Requires [Quarto](https://quarto.org/docs/get-started/).

```bash
quarto render        # build the site into docs/
quarto preview        # live-reloading local preview
```

## Deployment

Pushing to `main` triggers `.github/workflows/publish.yml`, which renders the site with Quarto and publishes it to the `gh-pages` branch. GitHub Pages must be set to serve from **GitHub Actions** (Settings → Pages → Source) rather than from a branch.

## Updating publications

1. Export citations from the [Google Scholar profile](https://scholar.google.com/citations?user=C28lZmUAAAAJ&hl=en) as CSV.
2. Run `python scripts/diff_citations.py path/to/export.csv` to see what's new or changed since the last import.
3. Update `research.qmd` (and add a `news/` post if it's worth announcing) by hand — classification (Academic / Working Paper / Policy) and summaries need a human judgement call, not just the raw citation data.
4. Once incorporated, run `python scripts/diff_citations.py path/to/export.csv --update-baseline` to reset the comparison point for next time.
