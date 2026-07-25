# Association for Constraint Programming (ACP) Website

Welcome to the static GitHub-hosted repository for the **Association for Constraint Programming (ACP)** website ([a4cp.org](https://www.a4cp.org)). This website is built using **Hugo** (a fast Static Site Generator) and the **PaperMod** theme.

## Why a Static Site?
Transitioning from the previous Drupal CMS to a static site hosted on GitHub provides several key benefits:
- **Zero Maintenance**: No database or CMS plugins to manage, ensuring long-term stability and security.
- **Fast Performance**: Light static HTML pages serve near-instantaneously worldwide.
- **Open Community Contributions**: Any community member or researcher can propose content updates directly through GitHub Pull Requests.

---

## How to Contribute (Open Pull Requests for Anyone)

**Anyone can contribute content updates to the ACP website!** You don't need programming expertise—all site pages, announcements, news items, and policies are written in standard **Markdown** (`.md` files) inside the [`content/`](content) directory.

### Step-by-Step Guide to Proposing a Change

1. **Fork the Repository**: 
   Click the **Fork** button at the top right of this repository to create your copy.
2. **Navigate to Content**:
   Open the `content/` folder in your fork. Directories match the site sections (e.g., `about/`, `events/`, `news/`, `awards/`, `policies/`, `theses/`).
3. **Edit or Add Markdown**:
   - To update an existing page, open its `index.md` file (for example `content/about/index.md`) and click the **pencil icon ✏️** on GitHub.
   - To add news or an article, create a `.md` file with Hugo frontmatter:
     ```yaml
     ---
     title: "New CP Announcement"
     date: 2026-07-25
     draft: false
     ---
     ```
4. **Commit & Submit Pull Request (PR)**:
   Commit your changes with a clear summary message, then click **Compare & Pull Request** to submit your contribution to the main ACP repository for maintainer review.

---

## Site Maintenance & Crawler Utilities

This repository contains a dedicated Python crawler script ([crawler.py](crawler.py)) to sync and migrate pages and media assets from the legacy site structure into clean Hugo Markdown files:

```bash
# Set up Python virtual environment and run the crawler
python3 -m venv venv
./venv/bin/pip install requests beautifulsoup4 markdownify
./venv/bin/python crawler.py
```

- **Markdown Output**: Content is structured cleanly in `content/<section>/index.md`.
- **Static Assets & Posters**: Images, conference posters, and documents are downloaded into `static/`.

---

## Local Development (For Maintainers & Contributors)

To run and preview the website locally on your computer:

1. Install [Hugo](https://gohugo.io/installation/) (Extended edition).
2. Clone this repository and initialize theme submodules:
   ```bash
   git clone https://github.com/a4cp/website.git
   cd website
   git submodule update --init --recursive
   ```
3. Start the local server:
   ```bash
   hugo server -D
   ```
4. Open **`http://localhost:1313`** in your web browser.
