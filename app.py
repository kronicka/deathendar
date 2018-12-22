from PIL import Image
from datetime import date


# Generating a calendar for days is less practical than weeks
# I'm leaving this stuff in until I refactor it into a more generic function/class
def calculate_days(*dob: int) -> int:
    """
        Calculate number of days left to live based on date of birth
        NOTE: This function was a mistake, but just in case you want to know the number of days I'm leaving it in
    """
    average_life_expectancy = 26098            # actually half a day above the average human life expectancy (71.5 yrs)

    days_lived = abs(date.today() - date(*dob)).days
    days_left = average_life_expectancy - days_lived

    return days_left


# def generate_calendar_days(days: int):
#     """ Generate a calendar based on the number of days """
#     days += 1
#     square_path = 'img/square.jpg'
#     background_path = 'img/background.png'
#     square_size = (50, 50)
#     cols = 48
#     rows = int(days / cols)
#
#     with Image.open(square_path) as square, Image.open(background_path) as background:
#         print(background.format, background.size, background.mode)
#         print(square.format, square.size)
#         square = square.resize(square_size)
#
#         for row in range(0, rows):
#             for col in range(0, cols):
#                 box = (square.size[0] * col + 20, square_size[1] * row + 20)
#                 background.paste(square, box)
#
#         background.show()


# Actually relevant code starts here
def calculate_weeks(*dob: int) -> int:
    average_life_expectancy = 3726      # actually about half a week above the average human life expectancy (71.5 yrs)

    weeks_lived = abs(date.today() - date(*dob)).days / 7
    weeks_left = average_life_expectancy - weeks_lived

    return int(weeks_left)


def generate_calendar(weeks: int):
    """ Generate a calendar based on the number of weeks """
    # TODO: scale square pics based on the number of weeks
    weeks += 1
    square_path = 'img/square.jpg'
    background_path = 'img/background.png'

    square_size = (50, 50)
    cols = 48
    padding = 40
    rows = int(weeks / cols)

    with Image.open(square_path) as square, Image.open(background_path) as background:
        print(background.format, background.size, background.mode)
        print(square.format, square.size)
        square = square.resize(square_size)

        for row in range(0, rows):
            for col in range(0, cols):
                box = (square.size[0] * col + padding, square_size[1] * row + padding)
                background.paste(square, box)

        background.show()


if __name__ == '__main__':
    weeks = calculate_weeks(1995, 4, 10)
    generate_calendar(weeks)
