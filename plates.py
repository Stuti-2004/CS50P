punctuation = ['!','.',',','-']

def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Match the length requirement
    if (len(s) < 2 or len(s) > 6):
        return False

    # No punctuation
    for i in punctuation:
        if i in s:
            return False

    # if the first two are not letters
    if (s[:2].isnumeric()):
        return False


    for i in s:
        if i.isdigit():
            index = s.index(i)
            if s[index:].isdigit() and int(i) != 0:
                return True
            else:
                return False
    else:
        return True
#Numbers cannot be used in the middle of a plate; they must come at the end. For example,
#AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”

main()