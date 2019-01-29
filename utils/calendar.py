import svgwrite
from wand.image import Image
from utils.constants import CAL_SIZE, CSS_STYLES


def draw_label(num_of_labels: int, dwg):
    """
    Draw units label for each starting week in a row.
    """
    x = 10
    y = 10
    for label in range(num_of_labels):
        dwg.add(dwg.text(label, insert=(x, y * label), font_size='2px', fill='grey'))


def generate_calendar_svg(units: int, file_format: str):
    """
    Generate an svg calendar based on the number of weeks
    """
    dwg = svgwrite.Drawing('calendar.svg', size=CAL_SIZE)
    dwg.viewbox(0, 0, 420, 594)
    dwg.defs.add(dwg.style(CSS_STYLES))

    dwg.add(dwg.rect(size=('100%', '100%'), fill='white', class_='background'))

    def group(classname):
        return dwg.add(dwg.g(class_=classname))
    squares = group('square')

    square_size = (5, 5)
    cols = 50
    padding = 11

    rows, leftover = divmod(units / cols, 1)
    rows = int(rows) + 1

    for row in range(0, rows):
        if row == rows - 1 and leftover != 0:
            cols *= leftover
            cols = int(cols)
        for col in range(0, cols):
            xc = col * 8 + padding
            yc = row * 8 + padding * 2
            square = dwg.rect(insert=(xc, yc), size=square_size)
            squares.add(square)

    # draw_label(rows, dwg)

    tagline = 'This is your life on a single sheet of paper.'
    units_label = f'{units} wks / {float("%.3g" % (units * 7 / 365))} yrs'
    dwg.add(dwg.text(tagline, insert=(180, 580), font_size='5px', fill='grey'))
    dwg.add(dwg.text(units_label, insert=(360, 580), font_size='5px', fill='grey'))
    dwg.save()

    if file_format != 'svg':
        with open('calendar.svg', mode='rb') as svg_file, Image(blob=svg_file.read(), format='svg') as image:
            png_image = image.make_blob('png')

        with open('calendar.png', mode='wb') as png_out:
            png_out.write(png_image)


if __name__ == '__main__':
    generate_calendar_svg(100, 'png')
