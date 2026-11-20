from PIL import Image, ImageDraw, ImageFont
import os

base = os.path.dirname(os.path.abspath(__file__))
font_path = "C:/Windows/Fonts/msyhbd.ttc"

for size in (192, 512):
    img = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.rounded_rectangle([0, 0, size - 1, size - 1], radius=int(size * 0.22), fill=(15, 157, 118, 255))
    m = int(size * 0.16)
    d.ellipse([m, m, size - m, size - m], outline=(255, 255, 255, 70), width=max(2, int(size * 0.035)))
    font = ImageFont.truetype(font_path, int(size * 0.46))
    text = "戒"
    box = d.textbbox((0, 0), text, font=font)
    w, h = box[2] - box[0], box[3] - box[1]
    x = (size - w) // 2 - box[0]
    y = (size - h) // 2 - box[1] - int(size * 0.01)
    d.text((x, y), text, font=font, fill=(255, 255, 255, 255))
    path = os.path.join(base, "icon-%d.png" % size)
    img.save(path)
    print("saved", path)
