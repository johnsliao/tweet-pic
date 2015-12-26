#!/usr/bin/python
import random

# Third-party dependencies
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

from config import *

def parse_text(quote, draw, font):
    lines = []
    line = ''

    for word in quote.split():
        # if added word goes over, create new line
        if draw.textsize(line+word,font)[0]>MAX_WIDTH:
            lines.append(line)
            line=''
            line+=word
            line+=' '
        else:
            line+=word
            line+=' '

    lines.append(line) # add last line

    return lines

def text2img(quote, author):

    # IMG SETTINGS (COLOR/FONT)
    FONT = FONT_NAME[random.randint(0,len(FONT_NAME))-1] # pick random font

    c = random.randint(0,len(COLOR_SCHEME)-1)
    BG_COLOR = COLOR_SCHEME[c]["bg"]
    FONT_COLOR = COLOR_SCHEME[c]["font_color"]

    # declare PIL objects
    font = ImageFont.truetype(FONT,FONT_SIZE)
    img=Image.new("RGBA", (CANVAS_WIDTH,CANVAS_HEIGHT),BG_COLOR)
    draw = ImageDraw.Draw(img)

    lines = parse_text(quote, draw, font)

    line_height = draw.textsize("T",font)[1] # use dummy char T to find line height

    # Create the img
    for num_lines in range(len(lines)):
        draw.text((20, START_HEIGHT+line_height*num_lines),lines[num_lines],FONT_COLOR,font=font)

    draw.text((20, START_HEIGHT+line_height*len(lines)+line_height),'-'+author,FONT_COLOR,font=font)

    img.save("quote_img.png")

if __name__=='__main__':
    text2img('He sells seashells down by the seashore','Albert Einstein')