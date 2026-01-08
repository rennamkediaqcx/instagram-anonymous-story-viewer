# Instagram Anonymous Story Viewer Automation

This repository is a developer-friendly template that demonstrates how privacy-oriented story viewing workflows can be organized.
It provides an orchestration layer for anonymous viewing, a best-effort incognito browser opener, and an optional saver for direct
media URLs you are permitted to download.

## Quickstart

### Install
```bash
pip install -r requirements.txt
```

### Run examples
```bash
python examples/anonymous_view.py
python examples/save_story.py
```

### Run tests
```bash
pytest -q
```

## Important notes
- This template does not bypass login or private account protections.
- It does not extract story media URLs from Instagram.
- Use only with content you are permitted to access and download.
