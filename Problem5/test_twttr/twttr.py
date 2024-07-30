def main():
    word = input("Input: ")
    # str can not be modified so we need an extra string to keep the result
    result = shorten(word)
    print("Output:", result)

def shorten(word):
    result = ""
    for s in word:
        if s in ["a","e","i","o","u","A","E","I","O","U"]:
            continue
        else:
            result += s
    return result

if __name__ == "__main__":
    main()
