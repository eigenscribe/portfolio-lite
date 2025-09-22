#!/usr/bin/env python3
"""
Build and optionally minify the Scriber Labs theme CSS bundle.
"""

import pathlib
import shutil
import subprocess
import sys

# ----------------------------------------------------------------------
# Paths
# ----------------------------------------------------------------------
ROOT = pathlib.Path(__file__).resolve().parents[1] # repo root
SRC_CSS = ROOT / "static" / "css"
BUILD_DIR = ROOT / "static" / "css" / "build" 

# ----------------------------------------------------------------------
# 1️⃣ Clean old build
# ----------------------------------------------------------------------
shutil.rmtree(BUILD_DIR, ignore_errors=True)
BUILD_DIR.mkdir(parents=True, exist_ok=True)

# ----------------------------------------------------------------------
# 2️⃣ Order of files (adjust if your filenames differ)
# ----------------------------------------------------------------------
ORDER = [
    "sections/profile.css",
    "sections/projects.css",
    "sections/future-content.css",
    "icons.css",
    "responsive-design.css",
]

# ----------------------------------------------------------------------
# 3️⃣ Concatenate – with defensive checks
# ----------------------------------------------------------------------
bundle_path = BUILD_DIR / "bundle.css" 

with bundle_path.open("w", encoding="utf-8") as out:
    for name in ORDER:
        src = SRC_CSS / name
        if not src.is_file():
            print(f"⚠️ Missing {src}", file=sys.stderr)
            continue        # skip missing files, keep going
        out.write(f"\n/* ----- {name} ----- */\n")
        out.write(src.read_text(encoding="utf-8"))
        out.write("\n")     # guarantee a trailing newline

print(f"✅ Bundle stylesheet created: {bundle_path}")