from datetime import datetime
from collections import defaultdict


users = {"Bill": datetime(year=2002, month=6, day=28),
         "Jill": datetime(year=2007, month=6, day=29),
         "Kitty": datetime(year=2005, month=6, day=29),
         "Kim": datetime(year=2000, month=7, day=1),
         "Jan": datetime(year=1995, month=8, day=30),
         "Sam": datetime(year=1992, month=1, day=30)
         }


def get_birthdays_per_week(users):
    current_datetime = datetime.now()
    this_week_birthday = defaultdict(list)
    for key, values in users.items():
        this_year_birthday = datetime(
            current_datetime.year, values.month, values.day)
        days_to_birthday = this_year_birthday - current_datetime
        if days_to_birthday.days < 0 or days_to_birthday.days > 6:
            continue
        weekday = this_year_birthday.strftime('%A')
        this_week_birthday['Monday' if weekday in [
            'Sunday', 'Saturday'] else weekday].append(key)
    for key, values in this_week_birthday.items():
        print(f"{key} : {', '.join(values)}")


def main():
    get_birthdays_per_week(users)
    return 0


if __name__ == "__main__":
    main()
