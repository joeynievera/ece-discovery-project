import os

from waveshare_epd import epd2in7

from PIL import Image
from PIL import ImageDraw

pic_dr = 'pic'

try:
    # start display
    epd_display = epd2in7.EPD()
    epd_display.init()

    # clear display
    epd_display.Clear(255)

    w = epd_display.height
    h = epd_display.width

    image = Image.new('1', (w, h), color = 255)
    draw = ImageDraw.Draw(image)

    kitty = Image.open('my_img.bmp')

    image.paste(kitty, (0, 0), kitty)

    epd_display.display(epd_display.getbuffer(image))

except IOError as e:
    print(e)
