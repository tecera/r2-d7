import os

from PIL import Image, ImageFont, ImageDraw, ImageOps

fonts = {
    'xwing-miniatures.ttf': {
        'sloopleft': "1",
        'kturn': "2",
        'sloopright': "3",
        'turnleft': "4",
        'stop': "5",
        'turnright': "6",
        'bankleft': "7",
        'straight': "8",
        'bankright': "9",
        'trollleft': ":",
        'trollright': ";",
    },
}
colours = {
    '': (0, 0, 0),
    'green': '#7CC33B',
    'red': '#E61713',
}

size = (128, 128)

if not os.path.exists('maneuvers'):
    os.mkdir('maneuvers')

for font, glyphs in fonts.items():
    font = ImageFont.truetype(font, 128)
    for name, glyph in glyphs.items():
        for colour_name, colour in colours.items():
            im = Image.new("RGBA", (300, 300), (255, 255, 255, 0))

            draw = ImageDraw.Draw(im)
            draw.text((100, 100), glyph, font=font, fill=colour)

            # remove unneccessory whitespaces if needed
            im = im.crop(ImageOps.invert(im.convert('RGB')).getbbox())

            # im = ImageOps.invert(im)
            im.thumbnail(size, Image.ANTIALIAS)

            background = Image.new('RGBA', size, (255, 255, 255, 0))
            background.paste(
                im,
                ((size[0] - im.size[0]) // 2, (size[1] - im.size[1]) // 2))

            # write into file
            background.save("maneuvers/{}{}.png".format(colour_name, name))
