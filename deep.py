msg = (input("What is the answer to the Great Question of Life, the Universe, and Everything? ")).strip().lower()

if (msg == "42" or msg == "forty-two" or msg == "forty two"):
    print("Yes")
else:
   print("No")