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
