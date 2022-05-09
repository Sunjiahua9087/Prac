MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    while True:
        password = input("> ")
        if len(password) > 6:
            print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
              "characters, and contain:")


        elif len(password) < 2:
            print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
              "characters, and contain:")
            password = input("> ")

            count_lower = 0
            count_upper = 0
            count_digit = 0
            count_special = 0
            for char in password:

                if char.isdigit():
                    count_digit += 1
                elif char.islower():
                    count_lower += 1
                elif char.isupper():
                    count_upper += 1
                elif char in SPECIAL_CHARACTERS:
                    count_special += 1


            if count_lower == 0 or count_upper == 0 or count_digit == 0:
                return False
        else:
            print("Your {}-character password is valid: {}".format(len(password), password))

main()
