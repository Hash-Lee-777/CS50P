def main():
    usr_input = input()
    # "sep" can only set the split symbol between several inputs, so the input should be splited first.
    # The unpacking operation (*) can extract multiple values from an iterable object (such as a list or tuple) and pass them as separate parameters to a function.
    print(*usr_input.split(), sep='...')

if __name__ == "__main__":
    main()
