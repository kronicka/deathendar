import svgwrite
from utils.constants import CAL_SIZE, CSS_STYLES


def generate_calendar_svg(units: int, unit_type: str = 'weeks'):
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

    if unit_type == 'days':
        square_size = (1, 1)
        cols = 240

    rows, leftover = divmod(units / cols, 1)
    rows = int(rows) + 1

    for row in range(0, rows):
        if row == rows - 1 and leftover != 0:
            cols *= leftover
            cols = int(cols)
        for col in range(0, cols):
            xc = col * 8 + padding
            yc = row * 8 + padding
            square = dwg.rect(insert=(xc, yc), size=square_size)
            squares.add(square)

    tagline = 'This is your life on a single sheet of paper.'
    units_label = f'{units} wks / {float("%.3g" % (units * 7 / 365))} yrs'
    dwg.add(dwg.text(tagline, insert=(180, 580), font_size='5px', fill='grey'))
    dwg.add(dwg.text(units_label, insert=(360, 580), font_size='5px', fill='grey'))
    dwg.save()


if __name__ == '__main__':
    generate_calendar_svg(100)
