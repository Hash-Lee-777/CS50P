def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # check the length, capitalize, start and end
    if not (2 <= len(s) <= 6 and s[:2].isalpha() and s.lower() != s):
        return False
    # check whether the str only contains alpha and number
    if not s.isalnum():
        return False
    # check the part of number whether s start with 0
    for i in range(0, len(s)):
        if s[i].isdigit():
            if s[i] == "0" and not s[i - 1].isdigit():
                return False
            if s[i] == "0" and i + 1 < len(s):
                return False
    return True

if __name__ == "__main__":
    main()
