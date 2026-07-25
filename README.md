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

## Automated Deployment (GitHub Actions & GitHub Pages)

This repository includes a GitHub Actions workflow located in [`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) that automatically builds and deploys the HTML static site on every `git push` to `master`:

1. **Automatic Hugo Build**: Runs Hugo extended to generate minified HTML, CSS, and JS static files.
2. **GitHub Pages Publishing**: Uses the official `actions/deploy-pages` action to deploy the site artifact to GitHub Pages.

> **Note for Repository Administrators**:
> To enable automatic publishing on GitHub:
> 1. Go to **Settings** -> **Pages** in the GitHub repository.
> 2. Under **Build and deployment** -> **Source**, select **GitHub Actions**.

