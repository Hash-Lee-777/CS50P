def main():
    sentense = input("Input: ")
    # str can not be modified so we need an extra string to keep the result
    result = ""
    for s in sentense:
        if s in ["a","e","i","o","u","A","E","I","O","U"]:
            continue
        else:
            result += s
    print("Output:", result)
main()
