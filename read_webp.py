from PIL import Image

def convert_webp(webp):
    im = Image.open(webp).convert("RGB")
    return im