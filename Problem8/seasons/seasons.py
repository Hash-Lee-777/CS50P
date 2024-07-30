from datetime import date
from datetime import timedelta
import inflect
import sys

def trans(born_date, today_date):
    # 2. sub
    final = today_date - born_date
    minutes = final.days * 1440
    return minutes

def main():
    # 1. get the input born date and today
    try:
        born_date = date.fromisoformat(input("Date of Birth: "))
    except ValueError:
        sys.exit("Invalid date")
    today_date = date.today()
    final = trans(born_date, today_date)
    p = inflect.engine()
    words = p.number_to_words(final, andword="").capitalize()
    print(f"{words} minutes")

if __name__ == "__main__":
    main()
