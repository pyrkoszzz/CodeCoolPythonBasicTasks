def sort_user_list(num_list: list[int]) -> list[int]:
    return sorted(num_list)


def get_user_input() -> list[int]:
    user_input = input('Give numbers: ').split()
    user_nums = []
    try:
        user_nums = [int(x) for x in user_input]
    except ValueError:
        print("One of numbers are not correct!")
    return user_nums


user_int_list = get_user_input()
print(sort_user_list(user_int_list))