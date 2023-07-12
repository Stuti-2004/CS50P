
while(True):
    try :
        x, y = input("Fraction: ").split("/")
        x = int(x)
        y = int(y)

        if (x <= y and y != 0):
            if (x/y >= 0.99):
                print("F")
                break
            elif(x/y <= 0.01):
                print("E")
                break
            else:
                percent = round((x / y) * 100,2)
                print(int(percent), end="")
                print("%")
                break

    except (ValueError, ZeroDivisionError):
        continue