import svgwrite
from constants import CAL_SIZE, CSS_STYLES


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

    square_size = (8, 8)
    cols = 40
    padding = 10

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
            xc = col * 10 + padding
            yc = row * 10 + padding
            square = dwg.rect(insert=(xc, yc), size=square_size)
            squares.add(square)

    dwg.save()


if __name__ == '__main__':
    generate_calendar_svg(100)
