# Simple Captcha Image Generator In Python - IRM

from PIL import Image, ImageDraw, ImageFont
import random,string

width = 225
height = 50

code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))
print('Captcha code: {}'.format(code))
image = Image.new('RGB', (width, height), (255, 255, 255))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('font.ttf', 36)

code_chars = list(code)
for i, c in enumerate(code_chars):
    x = 10 + i * 30 + random.randint(-5, 5)
    y = 10 + random.randint(-5, 5)
    draw.text((x, y), c, font=font, fill=(0, 0, 0))

line_count = random.randint(15, 25)
for i in range(line_count):
    x1 = random.randint(0, width)
    y1 = random.randint(0, height)
    x2 = random.randint(0, width)
    y2 = random.randint(0, height)
    draw.line((x1, y1, x2, y2), fill=(0, 0, 0))

dot_count = random.randint(500, 1000)
for i in range(dot_count):
    x = random.randint(0, width)
    y = random.randint(0, height)
    draw.point((x, y), fill=(0, 0, 0))

image.save("captcha.png")


## optional
Image.open("captcha.png").show()

input("Done.")