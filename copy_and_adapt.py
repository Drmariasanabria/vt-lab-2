import os
import re

src_dir = "/Users/mariasanabria/Documents/Codex/2026-05-18/p-gale-esto-a-codex-text"
dest_dir = "/Users/mariasanabria/Documents/Codex/vt-lab-2"

# 1. Adapt global.css -> style.css
with open(f"{src_dir}/assets/css/global.css", "r") as f:
    css = f.read()

# Replace colors
css = css.replace("--cyan: #65e7ff;", "--cyan: #ff4d6d;") # Light red
css = css.replace("--lime: #b9ff72;", "--lime: #ffffff;") # White accent
css = css.replace("--rose: #ff6fbd;", "--rose: #BA0C2F;") # UNICAN Maroon
css = css.replace("--violet: #8e7cff;", "--violet: #8B0000;") # Dark red

# Write adapted CSS
os.makedirs(f"{dest_dir}/assets/css", exist_ok=True)
with open(f"{dest_dir}/assets/css/style.css", "w") as f:
    f.write(css)

# 2. Copy JS files
os.makedirs(f"{dest_dir}/assets/js", exist_ok=True)
import shutil
for js_file in ["firebase.js", "vtlab-ui.js", "portal.js"]:
    shutil.copy2(f"{src_dir}/assets/js/{js_file}", f"{dest_dir}/assets/js/{js_file}")

print("Assets copied and adapted.")
