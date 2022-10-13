from PIL import Image, ImageDraw, ImageFont


def get_ascii_char(r, g, b, ascii_chars):
    length = len(ascii_chars)
    gray = r * 0.299 + g * 0.587 + b * 0.114
    group_size = 256 / length
    return ascii_chars[int(gray / group_size)]


def get_txtimg(path, font_path="msyh.ttc", scale=10):
    img = Image.open(path)
    ascii_chars = list(r"/\|()1{}$@B%8&WM#ZO0QLCJUYX*hkbdpqwmoahkbdpqwmzcvunxrjft[]?-_+~<>i!lI;:,\"^`'. ")
    width, height = img.size
    new_img = Image.new("RGB", (width * scale, height * scale), color=(255, 255, 255))
    draw = ImageDraw.Draw(new_img)
    font = ImageFont.truetype(font_path)
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            draw.text((j * scale, i * scale),
                      get_ascii_char(*img.getpixel((j, i)), ascii_chars), (0, 0, 0), font=font)
    return new_img


def get_imgtxt(img, path):
    ascii_chars = list(r"/\|()1{}$@B%8&WM#ZO0QLCJUYX*hkbdpqwmoahkbdpqwmzcvunxrjft[]?-_+~<>i!lI;:,\"^`'. ")
    txt = ""
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            txt += get_ascii_char(*img.getpixel((j, i)), ascii_chars) + " "
        txt += "\n"
    with open(path, 'w+') as f:
        f.write(txt)



