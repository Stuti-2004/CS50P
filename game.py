import random
import sys

while True:
    try:
        n = int(input("Level:"))
        if (n > 0):
            integer = random.randint(1, n)

            while True:
                guess = int(input("Guess: "))
                if (guess > 0):
                    if (guess == integer):
                        print("Just right!")
                        sys.exit()

                    elif (guess < integer):
                        print("Too small!")

                    elif (guess > integer):
                        print("Too large!")
    except ValueError:
        pass