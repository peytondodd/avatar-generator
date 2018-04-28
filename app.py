"""
    app.py

    Entry point for python avatar generation program.
    By Toby Jordan, April 2018
    MIT License
"""

import turtle
import io
import string
import sys
import json
from PIL import Image, ImageOps
from random import randint as rand

# Setup
width, height = 8, 8
swidth, sheight = width*60, height*60
turtle.setup(swidth, sheight)
turtle.speed(0)
turtle.hideturtle()
turtle.pencolor('')

pal = [
    "#000000",
    "#000000",
    "#000000",
    "#0CAFEB",
    "#F5D718",
    "#EB63E2",
    "#A1FF4A"
]

with open('map.json') as f:
    cmap = json.load(f)

# Avatar Generation functions
def shift(ch, offset):
    return string.ascii_letters[(string.ascii_letters.index(ch)+offset)%len(string.ascii_letters)]

def pad(raw, size):
    if len(raw) > size:
        return raw[:size]
    else:
        padded = ''
        counter = 0
        while len(padded) < size:
            counter = 0 if len(raw) == counter else counter
            padded += raw[counter]
            counter += 1
        return padded

def write_cmap():
    cmap = {
        char: rand(0, 5) for char in string.ascii_letters
    }
    with open('map.json', 'w') as f:
        f.write(json.dumps(cmap))

def generate_avatar(rawstring):
    global width, height
    return [
        [
            pal[cmap[shift(ch, x+i)]] for x, ch in enumerate(pad(rawstring, width))
        ] for i in range(height)
    ]

# Avatar rendering functions
def pixel(col):
    turtle.fillcolor(col)
    turtle.pencolor(col)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(swidth/width)
        turtle.right(90)
        turtle.forward(sheight/height)
        turtle.right(90)
    turtle.end_fill()
    turtle.forward(swidth/width)

def render(asset):
    turtle.penup()
    turtle.goto(-swidth//2, sheight//2)
    turtle.pendown()

    for y in range(height):
        for x in range(width):
            pixel(asset[y][x])
        turtle.right(90)
        turtle.forward(sheight/height)
        turtle.right(90)
        turtle.forward(swidth)
        turtle.setheading(0)


# Image manipulation functions
def save(filename):
    ps = turtle.getscreen().getcanvas().postscript()
    im = Image.open(io.BytesIO(ps.encode('utf-8')))
    im.thumbnail((512, 512))
    cropped = im.crop((3, 3, 480, 480))
    cropped.save('./{}.png'.format(filename))

# Main functionality
def main():
    if len(sys.argv) < 2:
        print("Usage: gavpls <string> <filename:optional>")
        return
    else:
        rawstring = sys.argv[1]
        filename = sys.argv[2] if len(sys.argv) > 2 else "output"
        filename = filename[:filename.index(".")] if "." in filename else filename
    avatar = generate_avatar(rawstring)
    render(avatar)
    save(filename)

if __name__ == "__main__":
    main()