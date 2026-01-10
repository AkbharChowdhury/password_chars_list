import os
from dotenv import load_dotenv

load_dotenv()


def get_password_chars_list(chars_index: list[int]) -> map:
    password: str = os.getenv('PASSWORD')
    return map(lambda i: password[i - 1], chars_index)


def main() -> None:
    chars_index_list: list[str] = list(get_password_chars_list(chars_index=[1, 2]))
    print(chars_index_list)


if __name__ == '__main__':
    main()
