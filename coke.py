price = 50
coins = 0

while (coins < price):
    print("Amount Due:", price - coins)
    user_input = int(input("Insert Coin:"))
    if (user_input == 25 or user_input == 5 or user_input == 10):
        coins += user_input

print("Change Owed:", coins - price)