from PIL import Image


def calculate_days(*dob) -> int:
    """ Calculate number of days left to live based on date of birth """
    return 3


def generate_calendar(days: int):
    """ Generate a calendar based on the number of days """
    # TODO: scale square pics based on the number of days
    with Image.open('square.jpg') as square, Image.open('background.png') as background:
        print(background.format, background.size, background.mode)

        for day in range(days):
            box = (square.size[0] * day + 20, 0)
            background.paste(square, box)

        background.show()


if __name__ == '__main__':
    days = calculate_days(10, 10, 1995)
    generate_calendar(days)
