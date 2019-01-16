from PIL import ImageFont
from platform import system

# Constants
# Life Expectancy (2016 WB Data)
GENERAL_LIFE_EXPECTANCY_DAYS = 26097.5
GENERAL_LIFE_EXPECTANCY_WEEKS = 3728.214        # ~71.5 years
FEMALE_LIFE_EXPECTANCY_WEEKS = 3872.18071       # ~74.261 years
MALE_LIFE_EXPECTANCY_WEEKS = 3647.54929         # ~69.953 years

# Image Paths
SQUARE_PATH = 'img/square.jpg'
BACKGROUND_PATH = 'img/background.png'

# Text Draw Utilities
DARK_GREY = (192, 192, 192)
MACOS_FONT_PATH = '/Library/Fonts/Arial.ttf'
WINDOWS_FONT_PATH = 'arial.ttf'
PATH = WINDOWS_FONT_PATH if system() == 'Windows' else MACOS_FONT_PATH
FONT = ImageFont.truetype(PATH, 24)

# SVG calendar generation constants
CAL_WIDTH = '420mm'
CAL_HEIGHT = '594mm'
CAL_SIZE = (CAL_WIDTH, CAL_HEIGHT)
CSS_STYLES = """
    .square { fill: white; stroke: black; stroke-width: .1mm; padding: .1mm; }
"""