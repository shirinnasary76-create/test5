"""Create compact web copies, preserving all original site assets.

Photos keep their content, dimensions, colors and aspect ratio. Brand graphics
are exported at >=3x their displayed header/footer size. No overlays or filters.
"""
from pathlib import Path
from io import BytesIO
from PIL import Image, ImageOps
import json

ROOT = Path('/home/user')
ASSETS = ROOT / 'public/assets'
DEST = ASSETS / 'web'
DEST.mkdir(exist_ok=True)
asset_map = {}
original_total = web_total = 0

for source in sorted(ASSETS.glob('*.jpg')):
    if source.stat().st_size < 15000:
        continue
    image = ImageOps.exif_transpose(Image.open(source)).convert('RGB')
    output = BytesIO()
    image.save(output, format='JPEG', quality=88, optimize=True, progressive=True)
    data = output.getvalue()
    if len(data) >= source.stat().st_size * .96:
        continue
    target = DEST / source.name
    target.write_bytes(data)
    asset_map[source.name] = str(target.relative_to(ASSETS))
    original_total += source.stat().st_size
    web_total += len(data)

for name, height in [('logo-mark.png', 210), ('logo-text.png', 96), ('logo-full.png', 210)]:
    source = ASSETS / name
    image = Image.open(source).convert('RGBA')
    image.thumbnail((5000, height), Image.Resampling.LANCZOS)
    target = DEST / name
    image.save(target, optimize=True)
    asset_map[name] = str(target.relative_to(ASSETS))
    original_total += source.stat().st_size
    web_total += target.stat().st_size

(ROOT / 'src/web-asset-map.json').write_text(json.dumps(asset_map, indent=2) + '\n')
print(f'Prepared {len(asset_map)} optimized web assets: {original_total:,} -> {web_total:,} bytes. Original files preserved.')
