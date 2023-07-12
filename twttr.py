word = input("Input: ")
vowels = ['a', 'e' , 'i' , 'o', 'u', 'A', 'E', 'I', 'O', 'U']
new_word = ""

for i in word:
    if (i in vowels):
        continue
    else:
        new_word += i

print("Output: ", new_word)