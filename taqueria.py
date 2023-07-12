menu = {
    "baja taco": 4.00,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

total_price = 0

while True:
    try:
        choice = (input("Item:")).lower()

        if choice in menu:
            total_price += menu[choice]
            print("Total: ${:.2f}".format(total_price))

    except EOFError:
        print("\n")
        break

    except(KeyError):
        pass