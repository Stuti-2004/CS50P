x, y, z = input("Epression: ").split(" ")
x = int(x)
z = int(z)

if (y == "+"):
    print (float(x + z))

elif (y == "-"):
    print (float(x - z))

elif (y == "*"):
    print (float(x * z))

elif (y == "/"):
    print (float(x / z))
#cs50/problems/2022/python/interpreter