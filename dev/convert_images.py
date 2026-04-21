#!/usr/bin/env python3
import sys
import os
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("Pillow manquant — installe avec : pip install Pillow --break-system-packages")
    sys.exit(1)

QUALITY = 85
EXTENSIONS = {".png", ".jpg", ".jpeg"}

def convert_dir(source_dir):
    source = Path(source_dir)
    if not source.is_dir():
        print(f"Dossier introuvable : {source_dir}")
        sys.exit(1)

    files = [f for f in source.iterdir() if f.suffix.lower() in EXTENSIONS]
    if not files:
        print("Aucune image PNG/JPG trouvée.")
        return

    total_before = total_after = 0

    for img_path in sorted(files):
        size_before = img_path.stat().st_size
        webp_path = img_path.with_suffix(".webp")

        with Image.open(img_path) as img:
            img.save(webp_path, "WEBP", quality=QUALITY)

        size_after = webp_path.stat().st_size
        gain = (1 - size_after / size_before) * 100

        bak_path = img_path.with_suffix(img_path.suffix + ".bak")
        img_path.rename(bak_path)

        total_before += size_before
        total_after += size_after

        print(f"{img_path.name} -> {webp_path.name}  {size_before//1024}Ko -> {size_after//1024}Ko  ({gain:+.1f}%)")

    total_gain = (1 - total_after / total_before) * 100
    print(f"\nTotal : {total_before//1024}Ko -> {total_after//1024}Ko  ({total_gain:+.1f}%)")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python convert_images.py <dossier>")
        sys.exit(1)
    convert_dir(sys.argv[1])
