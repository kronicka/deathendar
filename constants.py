from PIL import ImageFont
from platform import system

# Constants
# Life Expectancy (2016 WB Data)
general_life_expectancy_days = 26097.5
general_life_expectancy_weeks = 3728.214        # ~71.5 years
female_life_expectancy_weeks = 3872.18071       # ~74.261 years
male_life_expectancy_weeks = 3647.54929         # ~69.953 years

# Text Draw Utilities
dark_grey = (192, 192, 192)
linux_font_path = '/Library/Fonts/Arial.ttf'
windows_font_path = 'arial.ttf'
path = windows_font_path if system() == 'Windows' else linux_font_path
font = ImageFont.truetype(path, 24)
