import sys

def main():
    print(gauge(convert(input("Fraction: "))))

def convert(fraction):
    while True:
        try:
            x, y = map(int, fraction.split("/"))
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError
            # round is used to clear the dot in for example 25.0
            return round(x / y * 100)
        except (ValueError, ZeroDivisionError):
            pass

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
