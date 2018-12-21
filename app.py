from PIL import Image
from datetime import date


def calculate_days(*dob: int) -> int:
    """ Calculate number of days left to live based on date of birth """
    average_life_expectancy = 26098         # actually half a day above the average human life expectancy (71.5 yrs)
    days_lived = abs(date.today() - date(*dob)).days
    days_left = average_life_expectancy - days_lived

    return days_left


def generate_calendar(days: int):
    """ Generate a calendar based on the number of days """
    # TODO: scale square pics based on the number of days
    square_path = 'img/square.jpg'
    background_path = 'img/background.png'
    with Image.open(square_path) as square, Image.open(background_path) as background:
        print(background.format, background.size, background.mode)

        for day in range(days):
            box = (square.size[0] * day + 20, 0)
            background.paste(square, box)

        background.show()


if __name__ == '__main__':
    days = calculate_days(1995, 10, 10)
    # generate_calendar(days)
