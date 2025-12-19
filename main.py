import os
from dotenv import load_dotenv
load_dotenv()
def main():
    my_password: str = os.getenv('PASSWORD')
    num_indexes = [8, 17, 18]
    password_chars: list[str] = [my_password[n - 1] for n in num_indexes]
    print(password_chars)

if __name__ == '__main__':
    main()
