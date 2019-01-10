from utils import constants
from PIL import Image
from PIL import ImageDraw


def draw_text(img: Image) -> None:
    """
    Draw a tagline on the bottom of the generated image.
    """
    text = 'This is your life on a single sheet of paper.'
    draw = ImageDraw.Draw(img)
    padding_left = 226        # The almost exact estimated half of pixel width of the current default tagline
    padding_bottom = 40
    draw.text(((img.size[0] / 2) - padding_left, img.size[1] - padding_bottom),
              text, constants.dark_grey, font=constants.font)


def draw_units_number(img: Image, units: int, unit_type: str) -> None:
    """
    Draw the life expectancy in specified units in the right corner of the generated image.
    """
    text = str(units) + ' ' + unit_type
    draw = ImageDraw.Draw(img)
    padding_left = 170
    padding_bottom = 40
    draw.text((img.size[0] - padding_left, img.size[1] - padding_bottom),
              text, constants.dark_grey, font=constants.font)