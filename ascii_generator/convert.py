from PIL import Image
import numpy as np

CHARSETS = {
    "dense": "@%#*+=-:. ",
    "sparse": "#O+=- ",
    "binary": "10"
}

def get_ascii_char(pixel_value, charset):
    scale = len(charset)
    return charset[int(pixel_value / 255 * (scale - 1))]

def image_to_ascii(path, width=100, charset_name='dense'):
    charset = CHARSETS.get(charset_name, CHARSETS['dense'])
    img = Image.open(path).convert('L')
    w, h = img.size
    aspect_ratio = h / w
    height = int(aspect_ratio * width * 0.55)
    img = img.resize((width, height))
    
    pixels = np.array(img)
    ascii_img = np.vectorize(lambda px: get_ascii_char(px, charset))(pixels)
    lines = ["".join(row) for row in ascii_img]
    return "\n".join(lines)
