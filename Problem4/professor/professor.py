import random

def main():
    correct = False
    score = 0
    level = get_level()
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        for _ in range(3):
            calculate = int(input(f"{x} + {y} = "))
            if answer == calculate:
                correct = True
                score += 1
                break
            else:
                print("EEE")
                continue
        if not correct:
            print(f"{x} + {y} = {answer}")
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                raise ValueError
            else:
                return level
        except ValueError:
            continue

def generate_integer(level):
    if level == 1:
        return random.choice(list(range(0,10)))
    elif level == 2:
        return random.choice(list(range(10,100)))
    elif level == 3:
        return random.choice(list(range(100,1000)))

if __name__ == "__main__":
    main()
