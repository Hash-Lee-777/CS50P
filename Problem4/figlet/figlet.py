from pyfiglet import Figlet
import random
import sys

def main():
    figlet = Figlet()
    # first consider the number of arg
    if len(sys.argv) == 1:
        font = random.choice(figlet.getFonts())
    elif len(sys.argv) == 3:
        # do not forget to check the legalty of agrv[1]
        if sys.argv[2] in figlet.getFonts() and sys.argv[1] in ["-f", "--font"]:
            font = sys.argv[2]
        else:
            sys.exit("Invalid args")
    else:
        sys.exit("The number of args is wrong")
    text = input("Input: ")
    figlet.setFont(font=font)
    print(f"Output:\n", figlet.renderText(text))

if __name__ == "__main__":
    main()
