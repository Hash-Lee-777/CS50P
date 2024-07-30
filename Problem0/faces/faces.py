def convert(sentense):
    sentense = sentense.replace(":)", "🙂")
    return sentense.replace(":(", "🙁")

def main():
    sentense = input()
    sentense = convert(sentense)
    print(sentense)

if __name__ == "__main__":
    main()
