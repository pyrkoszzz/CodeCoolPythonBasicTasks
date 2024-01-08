from datetime import datetime


def get_user_input() -> int:
    user_str = input("Input birth year: ")
    try:
        user_birth_year = int(user_str)
        return user_birth_year
    except ValueError:
        print("Given argument is not a number!")


def calculate_age(birth_year: int) -> int:
    current_year = datetime.now().year
    age = current_year - birth_year
    if age < 0:
        print("Invalid birth_year")
        return -1
    return current_year - birth_year
