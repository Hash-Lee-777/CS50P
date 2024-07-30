def main():
    time = input("What time is it? ")
    final_time = convert(time)
    if 7 <= final_time <= 8:
        print("breakfast time")
    elif 12 <= final_time <= 13:
        print("lunch time")
    elif 18 <= final_time <= 19:
        print("dinner time")
    else:
        return

def convert(time):
    hour, minute = time.split(":")
    final_time = float(hour) + float(minute) / 60
    return final_time

if __name__ == "__main__":
    main()
