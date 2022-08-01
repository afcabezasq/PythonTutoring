import random

def generate_password():
    letters = "abcdefghijklmnopq"
    uppercase_letters = letters.upper()
    symbols = "!#$%&?()_"
    numbers = "1234567890"
    characters = letters+uppercase_letters+symbols+numbers
    characters = list(characters)

    password = ""
    for i in range(0,8):
        random_character = random.choice(characters)
        password += random_character

    return password

def generator():
    password = generate_password()

    print(f"Your new password is : {password}")


if __name__ == '__main__':
    generator()