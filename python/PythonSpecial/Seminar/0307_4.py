from datetime import datetime as dt


def date_is_valid(date: str):
    try:
        dt.strptime(date, "%d.%m.%Y")
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    print(date_is_valid("29.02.2019"))
    print(date_is_valid("29.02.2018"))
    print(date_is_valid("29.02.2017"))
    print(date_is_valid("29.02.2016"))

