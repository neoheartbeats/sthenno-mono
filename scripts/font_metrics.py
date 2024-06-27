from fontTools.ttLib import TTFont


def print_font_metrics(font_path):
    font = TTFont(font_path)
    hhea = font["hhea"]
    os2 = font["OS/2"]

    print(f"Leading: {hhea.ascent - hhea.descent + hhea.lineGap}")


font_path = "/Users/sthenno/Library/Fonts/SthennoMono-Regular.ttf"
print_font_metrics(font_path)
