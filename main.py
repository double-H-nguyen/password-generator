from random import randint
from random import sample


def main():
    # Ask user for password variety type and length
    password_choice = input("Type 1 if you want uppercase only\n"
                            "Type 2 if you want both uppercase and lower case\n"
                            "Type 3 if you want all symbols\n")
    length = int(input("Choose the length of your password (number only): "))

    # Provide password based on chosen type and length
    if password_choice == "1":
        password = uppercase_only(length)
        print(f"\nHere is your password: {password}")
    elif password_choice == "2":
        password = upper_and_lowercase(length)
        print(f"\nHere is your password: {password}")
    elif password_choice == "3":
        password = all_symbols_ver2(length)
        print(f"\nHere is your password: {password}")
    else:
        print("\nThat's not one of the three choices. Sorry!")


def uppercase_only(length):
    # all upper case password
    password = ""
    for i in range(length):
        i = chr(randint(65, 90))
        password = str(password) + i
    return password


def upper_and_lowercase(length):
    # upper and lowercase password
    password = ""
    for i in range(int(length / 2)):
        i = chr(randint(65, 90))
        j = chr(randint(65, 90)).lower()
        password = str(password) + i + j
    return password


def all_symbols_ver2(length):
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase_letters = uppercase_letters.lower()
    digits = "0123456789"
    symbols = "()[]{},;:.-_/?+*#"

    upper, lower, nums, syms = True, True, True, True

    all = ""

    if upper:
        all += uppercase_letters
    if lower:
        all += lowercase_letters
    if nums:
        all += digits
    if syms:
        all += symbols

    password = "".join(sample(all, length))
    return password


if __name__ == "__main__":
    main()
