
# Mastermind Game

# This is a game created by Andrea Foralosso

MAX_NR_DIGITS = 5
LIST_DIGITS = list(range(0,10))

import random

def get_combination_to_guess():
    while True:
        number_of_digits = input(f"How many digits should have the combination to guess (1-{MAX_NR_DIGITS})?")
        if number_of_digits.isnumeric():
                number_of_digits = int(number_of_digits)
                if 1 <= number_of_digits <= MAX_NR_DIGITS:
                    list_possible_digits = LIST_DIGITS[:]
                    list_combination_to_guess = []
                    for _ in range(0,number_of_digits):
                        a = random.choice(list_possible_digits)
                        list_possible_digits.remove(a)
                        list_combination_to_guess.append(a)
                    break
                else:
                    print(f"Provide a positive number between 1 and {MAX_NR_DIGITS}")
    return number_of_digits, list_combination_to_guess


def get_tentative_from_user_as_list(number_of_digits_to_respect):
    while True:
        user_tentative = input(f"Insert a number with {number_of_digits_to_respect} different digits: ")
        if user_tentative.isnumeric():
            user_tentative = [int(x) for x in str(user_tentative)]
            if len(user_tentative) == number_of_digits_to_respect:
                break
            else:
                print(f"You need to insert a number with {number_of_digits_to_respect} different digits")
        else:
            print("Only numbers are allowed")
    return user_tentative


def check_input_user(user_tentative, combination_to_guess):
    if user_tentative == combination_to_guess:
        print("Congrats! You've won!")
        game_result = 1
    else:
        game_result = 0
        nr_stars = 0
        nr_bonus = 0
        for i in range(0,len(user_tentative)):
            if combination_to_guess[i] == user_tentative[i]:
                nr_stars = nr_stars + 1
            else:
                for x in combination_to_guess:
                    if user_tentative[i] == x:
                        nr_bonus = nr_bonus + 1
            i = i + 1
        print("There are: " + str(nr_stars) + " stars and " + str(nr_bonus) + " bonus")
    return game_result


def main():
    a = get_combination_to_guess()
    number_of_digits_to_respect = a[0]
    combination_to_guess = a[1]
    nr_tentative = 0
    while True:
        nr_tentative = nr_tentative + 1
        user_tentative = get_tentative_from_user_as_list(number_of_digits_to_respect)
        print(f"Your tentative has been: {user_tentative}")
        a = check_input_user(user_tentative, combination_to_guess)
        if a == 1:
            break
        else:
            print(f"You're unluck! Try again!! (Tentative nr {nr_tentative})")

main()

exit()