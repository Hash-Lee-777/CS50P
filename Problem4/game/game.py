import random
import sys

def main():
    while True:
        try:
            num = int(input("Level: "))
            if num > 0 :
                num_list = list(range(1, num + 1))
                answer = random.choice(num_list)
                while True:
                    guess_num = int(input("Guess: "))
                    if(guess_num > answer):
                        print("Too large!")
                        continue
                    elif(guess_num < answer):
                        print("Too small!")
                        continue
                    else:
                        print("Just right!")
                        sys.exit()
                break
        except (TypeError,ValueError):
            continue
main()
