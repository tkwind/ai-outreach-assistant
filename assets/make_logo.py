"""Render the 512x512 Agensi listing logo: score bars + paper plane on a gradient tile."""
from pathlib import Path
from PIL import Image, ImageDraw

S = 2048  # draw at 4x, downscale for smooth edges
top, bottom = (79, 70, 229), (20, 184, 166)  # indigo -> teal

grad = Image.new("RGB", (S, S))
px = grad.load()
for y in range(S):
    for x in range(S):
        t = (x + y) / (2 * S)
        px[x, y] = tuple(int(a + (b - a) * t) for a, b in zip(top, bottom))

mask = Image.new("L", (S, S), 0)
ImageDraw.Draw(mask).rounded_rectangle((0, 0, S - 1, S - 1), radius=420, fill=255)
img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
img.paste(grad, (0, 0), mask)

d = ImageDraw.Draw(img, "RGBA")
# ascending score bars
for x0, y0, a in [(400, 1360, 150), (620, 1180, 200), (840, 1000, 255)]:
    d.rounded_rectangle((x0, y0, x0 + 160, 1640), radius=48, fill=(255, 255, 255, a))
# paper plane
T, A, C, B, D = (1680, 420), (820, 860), (1200, 980), (1320, 1320), (1130, 1100)
d.polygon([T, A, C], fill=(255, 255, 255, 255))
d.polygon([T, C, B], fill=(235, 240, 255, 255))
d.polygon([C, B, D], fill=(200, 210, 245, 255))

out = Path(__file__).with_name("agensi-logo.png")
img.resize((512, 512), Image.LANCZOS).save(out)
print(out)
