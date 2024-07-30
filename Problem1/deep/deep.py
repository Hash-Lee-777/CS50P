def main():
    # strip is used to clear spaces on the side, lower is used to convery to an unified form.
    question = input("What is the answer to the Great Question of Life, the Universe, and Everything?").lower().strip()
    if question in ["42", "forty two", "forty-two"]:
        print("Yes")
    else:
        print("No")

main()
