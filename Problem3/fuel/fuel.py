while True:
    try:
        # convert
        x, y = map(int, input("Fraction: ").split("/"))
        if x > y:
            raise ValueError
        break
    except (ValueError, ZeroDivisionError):
        print("Invalid value, input it again")

# round is used to clear the dot in for example 25.0
percentage = round(x / y * 100)
if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(f"{percentage}%")
