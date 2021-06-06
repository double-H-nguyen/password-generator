from random import randint


def main():
    password = uppercase_only()
    # password = upper_and_lowercase()
    print(f"Here is your password: {password}")


def uppercase_only():
    # all upper case password
    password = ""
    for i in range(10):
        i = chr(randint(65, 90))
        password = str(password) + i
    return password


def upper_and_lowercase():
    # upper and lowercase password
    password = ""
    for i in range(5):
        i = chr(randint(65, 90))
        j = chr(randint(65, 90)).lower()
        password = str(password) + i + j
    return password


if __name__ == "__main__":
    main()
