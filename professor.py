'''
# PROBLEM SET 4
In a file called professor.py, implement a program that:
Prompts the user for a level, 
If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 
 digits. No need to support operations other than addition (+).
Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should 
output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still 
not answered correctly after three tries, the program should output the correct answer.
The program should ultimately output the user’s score: the number of correct answers out of 10.
Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 
    1, 2, or 3, and generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:
'''

import random
import sys
import os


def main():
    level = get_level()
    questions = 0
    correct = 0

    while questions < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        tries = 0
        questions += 1

        while True:
            print(f"{x} + {y} = ", end="")
            ans = input("")

            try:
                ans = int(ans)

                if ans == (x + y):
                    correct += 1
                    break

                else:
                    tries += 1
                    if tries >= 3:
                        print(f"{x} + {y} =", x + y)
                        break
                    else:
                        print("EEE")

            except ValueError:
                tries += 1
                if tries >= 3:
                    print(f"{x} + {y} =", x + y)
                    break
                else:
                    print("EEE")

    print("Score:", correct)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
