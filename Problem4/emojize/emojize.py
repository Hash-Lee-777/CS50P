import emoji

def main():
    icon = input("Input: ")
    print("Output: ", emoji.emojize(icon, language = "alias"))

if __name__ == "__main__":
    main()
