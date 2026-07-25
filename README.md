# Association for Constraint Programming (ACP) Website

Welcome to the static GitHub-hosted repository for the **Association for Constraint Programming (ACP)** website ([a4cp.org](https://www.a4cp.org)). This website is built using **Hugo** (a fast Static Site Generator) and the **PaperMod** theme.

---

## Website Structure & Content Table of Contents

All site content is stored as Markdown files inside the [`content/`](content) directory. Below is an overview of the content layout and structure:

```
content/
├── _index.md                        # Home Page (Welcome hero, ACP mission, quick links)
├── about/                           # About the ACP
│   ├── index.md                     # Overview & Executive Committee overview
│   ├── statutes/                    # ACP Statutes (English & French)
│   ├── bylaws/                      # ACP Bylaws
│   ├── committee/                   # Executive Committee members & election results
│   ├── committee/decisions/         # Executive Committee quarterly reports & meeting minutes
│   ├── general-assembly-archive/    # Minutes & reports from annual General Assemblies
│   └── acp-logo/                    # ACP official logo assets & guidelines
├── events/                          # Events & Activities
│   ├── index.md                     # Events summary
│   ├── cp-conference-series/        # Annual CP Conference series (posters, locations, proceedings)
│   ├── summer-schools/              # ACP Summer Schools archive & upcoming bids
│   ├── competitions/                # Solver & Model competitions (MiniZinc, CP Solver competitions)
│   └── outreach/                    # Community outreach initiatives
├── awards/                          # ACP Awards & Honors
│   ├── index.md                     # Awards overview
│   ├── research-excellence-award/   # Research Excellence Award recipients
│   ├── distinguished-service-award/ # Distinguished Service Award recipients
│   ├── early-career-research-award/ # Early Career Research Award recipients
│   ├── doctoral-research-award/    # Doctoral Research Award recipients
│   └── paper-awards/                # Best Paper Award recipients at CP conferences
├── news/                            # News & Announcements
│   ├── index.md                     # News section overview
│   ├── career-news/                 # Open positions, PhD/Postdoc opportunities
│   └── newsletters/                 # Historical ACP Quarterly Newsletters archive
├── cp/                              # Constraint Programming Resources
│   ├── success-stories/             # High-impact industrial & scientific CP application stories
│   ├── publication-venues/          # Primary CP journals, conferences, and publishing guidelines
│   └── application/papers/          # Selected CP application papers listing
├── theses/                          # PhD Thesis Archive
│   └── index.md                     # Repository of PhD dissertations in Constraint Programming
├── old_nodes/                       # Archived legacy Drupal nodes & articles
│   ├── index.md                     # Legacy nodes archive index
│   └── <node_id>/index.md           # Individual legacy Drupal articles & node pages
├── sponsorships-donations/          # Sponsorships & Financial Support
│   └── index.md                     # Guidelines for conference & summer school sponsorships
└── contact/                         # Contact Information
    └── index.md                     # Officers, email addresses, and secretary contact
```

---

## How to Contribute (Open Pull Requests for Anyone)

**Anyone can contribute content updates to the ACP website!** You don't need programming expertise—all site pages, announcements, news items, and policies are written in standard **Markdown** (`.md` files) inside the [`content/`](content) directory.

### Guidelines for Editing Content

- **Page Titles & Frontmatter**: Ensure every `.md` file starts with YAML frontmatter containing `title`, `date`, and `draft: false`.
- **Relative Links Only**: Always use relative URLs (e.g. `/events/cp-conference-series/` or `/about/bylaws/`). Never hardcode absolute `https://www.a4cp.org` URLs for internal pages.
- **Images & Attachments**: Store static images and downloadable PDF documents in [`static/`](static) and reference them with relative static paths (e.g., `/posters/2024.png` or `/sites/default/files/agm2025.pdf`).

### Step-by-Step Guide to Proposing a Change

1. **Fork the Repository**: 
   Click the **Fork** button at the top right of this repository to create your copy.
2. **Navigate to Content**:
   Open the `content/` folder in your fork. Find the relevant folder using the [Website Structure](#website-structure--content-table-of-contents) above.
3. **Edit or Add Markdown**:
   - To update an existing page, open its `index.md` file and click the **pencil icon ✏️** on GitHub.
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

## Local Development (For Maintainers & Contributors)

To run and preview the website locally on your computer:

1. Install [Hugo](https://gohugo.io/installation/) (Extended edition).
2. Clone this repository and initialize theme submodules:
   ```bash
   git clone git@github.com:a4cp-org/a4cp-org.github.io.git
   cd a4cp-org.github.io
   git submodule update --init --recursive
   ```
3. Start the local server:
   ```bash
   hugo server -D
   ```
4. Open **`http://localhost:1313`** in your web browser.

---

## Automated Deployment (GitHub Actions & `gh-pages` Branch)

This repository includes an automated GitHub Actions workflow located in [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) that builds the static site and updates the orphan **`gh-pages`** branch upon every commit to `master`:

1. **Automatic Hugo Compilation**: On every push to `master`, GitHub Actions compiles all Markdown content and assets into static HTML/CSS inside `./public`.
2. **Orphan `gh-pages` Branch Publishing**: The action automatically commits and pushes the compiled static HTML to the dedicated orphan **`gh-pages`** branch.
3. **GitHub Pages Configuration**:
   - Go to **Settings** -> **Pages** in the repository.
   - Under **Source**, select **Deploy from a branch**.
   - Choose Branch: **`gh-pages`** / Folder: **`/ (root)`**.

---

## Branch Protection (Prevent Direct Pushes to `gh-pages`)

To prevent contributors or maintainers from accidentally pushing code directly to the compiled `gh-pages` branch, enable GitHub Branch Protection Rules:

1. Go to **Settings** -> **Rules** -> **Rulesets** (or **Settings** -> **Branches**).
2. Click **New ruleset** -> **New branch ruleset** (or **Add branch protection rule**).
3. Set the **Ruleset name** / **Branch name pattern** to: `gh-pages`.
4. Under **Rules**, check **Block pushes** (or **Restrict pushes**). This prevents any human user from running `git push origin gh-pages`.
5. Under **Bypass list** (if using Rulesets), add **Repository admin** or **GitHub Actions** so that the workflow is permitted to publish updates.
6. Click **Save changes**.

Once this rule is active:
- Direct human commands (`git push origin gh-pages`) will be rejected with an error.
- The automated GitHub Actions workflow will continue to compile and update `gh-pages` automatically whenever changes are pushed to `master`.



