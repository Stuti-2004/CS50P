months = [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December"
        ]
while True:
    try:
        old_date = input("Date:")

        if "/" in old_date:
            month, date, year = old_date.split("/")
            month = int(month)
            date = int(date)
            year = int(year)

        else:
            month, date, year = old_date.split(" ")
            date = int(date[:-1])

            if (str(month) in months):
                month = months.index(month) + 1

            year = int(year)

        if (month <= 12 and date <= 31):
            print(year, f"{month:02}", f"{date:02}", sep="-")
            break

    except (KeyError):
        pass

    except ValueError:
        pass