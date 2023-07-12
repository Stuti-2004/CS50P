camel = input("camelCase: ")
snake_name = ""

for letter in camel:
    if (letter.isupper()):
        snake_name += ("_" + letter.replace(letter, letter.lower()))
    else:
        snake_name += letter

print("snake_case:", snake_name)

#check50 cs50/problems/2022/python/camel