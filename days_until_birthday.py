from datetime import datetime


def calculate_days_until_birthday(birthday: datetime) -> int:
    today = datetime.now()
    next_birthday = datetime(today.year, birthday.month, birthday.day)

    if today > next_birthday:
        next_birthday = datetime(today.year + 1, birthday.month, birthday.day)

    return (next_birthday - today).days


my_birthday = datetime(2003, 1, 3)
print(calculate_days_until_birthday(my_birthday))
