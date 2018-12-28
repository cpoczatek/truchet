#
#
#
import argparse
import drawSvg as draw
import random

def addTile(drawing, xposition, yposition, type, args):
    t = args.tile
    x = xposition * t
    y = yposition * t
    radius = t/2
    sw = args.stroke
    color = args.color
    if type == 'a':
        drawing.append(draw.Arc(x+t, y, radius, 90, 180, cw=False, stroke=color, stroke_width=sw, fill='none'))
        drawing.append(draw.Arc(x, y+t, radius, 0, 270, cw=True, stroke=color, stroke_width=sw, fill='none'))
    elif type == 'b':
        drawing.append(draw.Arc(x+t, y+t, radius, 180, 270, cw=False, stroke=color, stroke_width=sw, fill='none'))
        drawing.append(draw.Arc(x, y, radius, 0, 90, cw=False, stroke=color, stroke_width=sw, fill='none'))
    else:
        return

def addTiles(drawing, args):
    for x in range(args.width):
        for y in range(args.height):
            addTile(drawing, x, y, random.choice(('a','b')), args)

def addSquares(drawing, args):
    w = args.tile
    h = w
    for x in range(args.width):
        for y in range(args.height):
            xpos = x*w
            ypos = y*h
            drawing.append(draw.Rectangle(xpos, ypos, w, h, stroke='silver', stroke_width=1, fill='none'))

def setupArgs():
    parser = argparse.ArgumentParser(description='Generate svg of random truchet tiles.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--width', type=int, default=10,
                        help='Width of svg in tiles.')
    parser.add_argument('--height', type=int, default=10,
                        help='Height of svg in tiles.')
    parser.add_argument('--tile', type=int, default=40,
                        help='Size of tile in px.')
    parser.add_argument('--stroke', type=int, default=4,
                        help='Stroke width of arcs.')
    parser.add_argument('--color', type=str, default='navy',
                        help='Color of arcs. HTML colors are valid and should be **quoted**. Eg: "#800000", "rgb(0,255,0)", "blue"')
    parser.add_argument('--seed', type=int, default=42,
                        help='Seed value for PRNG.')
    parser.add_argument('--squares', action='store_true', help='Add tile boundaries, stroke=1/color="silver"')
    parser.add_argument('--output', type=str, default='truchet.svg',
                        help='Output filename')
    return parser

def main():
    parser = setupArgs()
    args = parser.parse_args()
    #
    random.seed(args.seed)
    d = draw.Drawing(args.width*args.tile, args.height*args.tile)
    addTiles(d, args)
    if args.squares:
        addSquares(d, args)
    d.saveSvg(args.output)


# ----------------------------
if __name__ == "__main__":
    main()
