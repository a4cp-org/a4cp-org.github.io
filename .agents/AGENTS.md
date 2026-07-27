# Agent Instructions & Guidelines

## Core Rule: No External Redirections to Old Website
- The site configuration and content **MUST NOT** redirect users to the old domain (`https://www.a4cp.org`).
- `baseURL` in `hugo.toml` must remain relative (i.e. `/`) so header menu links, breadcrumbs, and section pages resolve locally.
- All internal content links and menu item URLs must be relative paths (e.g., `/about/`, `/news/`, `/events/`) and never use absolute `https://www.a4cp.org` URLs.

## Core Rule: Keep README.md Updated with Content Structure Changes
- Whenever site content structure, section directories, or menu navigation changes are made in `content/` or `hugo.toml`, you **MUST** update `README.md` to reflect the changes in the Content Table of Contents and editing guidelines.
## Core Rule: Strict Menu Tree and Uniform Submenus
- The menu tree defined in `.agents/menu_tree.md` MUST be followed strictly.
- The presentation of the submenu (local navigation) MUST be uniform on each page within a section. It should display the entire hierarchical structure (including sub-items) of the active top-level menu item to ensure high-fidelity with the original site's local tasks.
