msg = input("Greeting: ").lower().strip()

if (msg.startswith("Hello") or msg.startswith("hello")):
    print("$0")
elif (msg.startswith("H") or msg.startswith("h")):
    print("$20")
else:
    print("$100")