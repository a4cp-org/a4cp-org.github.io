import os
import re
import shutil

moves = []
old_nodes_dir = "content/old_nodes"

for root, dirs, files in os.walk(old_nodes_dir):
    for file in files:
        if file.endswith(".md") and file != "_index.md":
            path = os.path.join(root, file)
            node_id = path.split("/")[-2]
            
            # extract title
            with open(path, "r") as f:
                content = f.read()
            title = ""
            if content.startswith("---"):
                frontmatter = content.split("---")[1]
                for line in frontmatter.splitlines():
                    if line.startswith("title:"):
                        title = line.split(":", 1)[1].strip().strip("\"'")
                        break
            
            # classify based on title
            lower_title = title.lower()
            new_path = ""
            if "quarterly report" in lower_title:
                # e.g., "2024 Quarterly Report 1"
                year_match = re.search(r"(\d{4})", title)
                q_match = re.search(r"(Report|Q)\s*(\d)", title, re.I)
                year = year_match.group(1) if year_match else "unknown"
                q = q_match.group(2) if q_match else "unknown"
                new_path = f"content/about/committee/decisions/report_{year}_q{q}.md"
            elif "volume " in lower_title and "number " in lower_title:
                # e.g., "Volume 9, Number 0, January 2013"
                vol_match = re.search(r"volume\s+(\d+)", lower_title)
                num_match = re.search(r"number\s+(\d+)", lower_title)
                vol = vol_match.group(1) if vol_match else "unknown"
                num = num_match.group(1) if num_match else "unknown"
                new_path = f"content/news/newsletters/vol{vol}_n{num}.md"
            elif "position" in lower_title or "postdoc" in lower_title or "opening" in lower_title or "professorship" in lower_title or "engineer on" in lower_title:
                safe_title = re.sub(r"[^\w\s-]", "", lower_title).strip().replace(" ", "_")[:30]
                new_path = f"content/news/career-news/{safe_title}.md"
            elif "impact" in lower_title or "comet" in lower_title or "self-assembling" in lower_title:
                safe_title = re.sub(r"[^\w\s-]", "", lower_title).strip().replace(" ", "_")[:30]
                new_path = f"content/cp/success-stories/{safe_title}.md"
            else:
                # Default to thesis/papers or general research if it looks like a paper
                safe_title = re.sub(r"[^\w\s-]", "", lower_title).strip().replace(" ", "_")[:30]
                new_path = f"content/theses/{safe_title}.md"
            
            if new_path:
                # Ensure unique new_path if collision
                base, ext = os.path.splitext(new_path)
                counter = 1
                final_new_path = new_path
                while any(m[1] == final_new_path for m in moves):
                    final_new_path = f"{base}_{counter}{ext}"
                    counter += 1
                
                moves.append((path, final_new_path, node_id))

# Now execute the moves and replace links
for old_path, new_path, node_id in moves:
    new_url = new_path.replace("content/", "/").replace(".md", "")
    old_urls = [f"/old_nodes/{node_id}", f"/-{node_id}"]
    
    # move file
    os.makedirs(os.path.dirname(new_path), exist_ok=True)
    shutil.move(old_path, new_path)
    
    # inject alias if missing just in case
    with open(new_path, "r") as f:
        content = f.read()
    if f"/old_nodes/{node_id}" not in content and f"/-{node_id}" not in content:
        if "aliases:" in content:
            content = content.replace("aliases:\n", f"aliases:\n  - /old_nodes/{node_id}\n")
        else:
            content = content.replace("---", f"---\naliases:\n  - /old_nodes/{node_id}", 1)
        with open(new_path, "w") as f:
            f.write(content)

    # update internal links across ALL markdown files
    for root_md, _, files_md in os.walk("content"):
        for file_md in files_md:
            if file_md.endswith(".md"):
                filepath = os.path.join(root_md, file_md)
                with open(filepath, "r") as f:
                    c = f.read()
                original_c = c
                
                for ou in old_urls:
                    c = c.replace(f"({ou})", f"({new_url})")
                    c = c.replace(f"({ou}/)", f"({new_url})")
                    c = c.replace(f"({ou} ", f"({new_url} ")
                    c = c.replace(f"href=\"{ou}\"", f"href=\"{new_url}\"")
                    c = c.replace(f"href=\"{ou}/\"", f"href=\"{new_url}\"")
                    c = c.replace(f"ref \"{ou}\"", f"ref \"{new_url}\"")
                    c = c.replace(f"ref \"{ou}/\"", f"ref \"{new_url}\"")
                
                if original_c != c:
                    with open(filepath, "w") as f:
                        f.write(c)

print(f"Successfully processed {len(moves)} nodes.")
