def main():
    str = input("camelCase: ")
    print("snake_case: ", end="")
    for s in str:
        s_lower = s.lower()
        if s != s_lower:
            s = "_"
            print(s + s_lower, end="")
        else:
            print(s,end="")
    print("")
main()
