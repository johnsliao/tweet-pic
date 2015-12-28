import random

# Third-party dependencies
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

from config import *

def parse_text(quote):
    # declare PIL objects
    img=Image.new("RGBA", (CANVAS_WIDTH,CANVAS_HEIGHT),BG_COLOR)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(FONT_NAME[0],FONT_SIZE)

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

    return lines, font, draw, img

if __name__=='__main__':
    tweet = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. " \
           "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. " \
           "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. " \
           "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum." \
            " #Lorem #ipsum #tweetpic"

    c = random.randint(0,len(COLOR_SCHEME)-1)

    BG_COLOR = COLOR_SCHEME[c]["bg"]
    FONT_COLOR = COLOR_SCHEME[c]["font_color"]

    done = False

    while(not done):
        lines, font, draw, img = parse_text(tweet)
        line_height = draw.textsize("T",font)[1] + draw.textsize("T",font)[1]/3 # dummy char T + in line buffer
        num_lines = len(lines)
        txt_height = line_height*num_lines

        if txt_height > MAX_HEIGHT: # too tall
            FONT_SIZE-=1
        else:
            Y=CANVAS_HEIGHT/2-txt_height/2 # center it
            done = True


    # Create the img
    for c in range(num_lines):
        x = X
        y = Y+line_height*c

        text = lines[c]

        draw.text((x, y),text, FONT_COLOR, font=font)

    img.save("tweet_img.png")