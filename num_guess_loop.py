#!/usr/bin/env python3

# Created by: Layla Michel
# Created on: May 26, 2021
# This program generates a random number between 0 and 9,
# asks the user to guess it, and displays whether they
# guessed correctly or not, while using a loop

import random


def main():
    # define variable
    correct_guess = random.randint(0, 9)

    while True:
        # get the user guess
        guess_as_string = input("Guess what number I\
 am thinking of between 0 and 9: ")

        try:
            # convert from string to integer
            guess_as_int = int(guess_as_string)

            if (guess_as_int < 0 or guess_as_int > 9):
                # check if number is within range
                print("{} is not within range, try again".
                      format(guess_as_int))
            else:

                if (guess_as_int == correct_guess):
                    print("You guessed correctly!")
                    print("Thanks for playing.")
                    break
                else:
                    print("{} is not the correct guess, try again.".
                          format(guess_as_int))

        except ValueError:
            # error message
            print("{} is not a valid number, try again.".
                  format(guess_as_string))


if __name__ == "__main__":
    main()
