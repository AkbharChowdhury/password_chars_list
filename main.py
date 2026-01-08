import os
from typing import Generator
from dotenv import load_dotenv

load_dotenv()


def get_password_chars_list(chars_index: list[int]) -> Generator[str]:
    password: str = os.getenv('PASSWORD')
    return (password[i - 1] for i in chars_index)


def main():
    chars_index_list: list[str] = list(get_password_chars_list(chars_index=[6, 9, 16]))
    print(chars_index_list)


if __name__ == '__main__':
    main()
