def main():
    time = input("What time is it? ")
    convertedtime = convert(time)

    if (7.0 <= convertedtime <= 8.0):
        print("breakfast time")

    elif (12.0 <= convertedtime <= 13.0):
        print("lunch time")

    if (18.0 <= convertedtime <= 19.0):
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    return(hours + minutes/60)


if __name__ == "__main__":
    main()