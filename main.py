import os
from dotenv import load_dotenv
load_dotenv()
def main():
    my_password: str = os.getenv('PASSWORD')
    num_indexes: list[int] = [1, 3]
    password_chars: list[str] = [my_password[n - 1] for n in num_indexes]
    print(password_chars)

if __name__ == '__main__':
    main()
# Untrack files

# Remove files
