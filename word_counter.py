def count_words(word: list[str]) -> int:
    return len(word)


def get_user_input() -> list[str]:
    return input("Input a sentence: ").split()


print(count_words(get_user_input()))
