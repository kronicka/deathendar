from utils import constants
from PIL import Image
from legacy.draw import draw_text, draw_units_number


def generate_calendar(units: int, unit_type: str = 'weeks'):
    """
    Generate a calendar based on the number of weeks
    """
    square_size = (50, 50)
    cols = 48
    padding = 40

    if unit_type == 'days':
        square_size = (10, 10)
        cols = 240
        padding = 40

    rows, leftover = divmod(units / cols, 1)
    rows = int(rows) + 1

    with Image.open(constants.SQUARE_PATH) as square, Image.open(constants.BACKGROUND_PATH) as background:
        print(background.format, background.size, background.mode)
        print(square.format, square.size)
        square = square.resize(square_size)

        for row in range(0, rows):
            if row == rows - 1 and leftover != 0:
                cols *= leftover
                cols = int(cols)
            for col in range(0, cols):
                box = (square.size[0] * col + padding, square_size[1] * row + padding * 2)
                background.paste(square, box)

        draw_text(background)
        draw_units_number(background, units, unit_type)
        background.save('calendar.png')
        background.show()
