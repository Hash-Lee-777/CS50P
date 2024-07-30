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
    "December",
]


while True:
    date = input("Date: ")
    # use / to create catogory
    if len(date.split("/")) == 3:
        date = date.split("/")
        try:
            month, day, year = map(int, date)
            if 1 <= month <= 12 and 1 <= day <= 31:
                print(f"{year:04d}-{month:02d}-{day:02d}")
                break
        # case October/9/1701 is contained in map(int, date) -> ValueError: invalid literal for int() with base 10: 'October'
        except ValueError:
            pass
    else:
        date = date.split(",")
        if len(date) == 2:
            try:
                month, day = date[0].split()
                month = months.index(month) + 1
                day, year = int(day), int(date[1])
                if 1 <= month <= 12 and 1 <= day <= 31:
                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    break
            except ValueError:
                pass
