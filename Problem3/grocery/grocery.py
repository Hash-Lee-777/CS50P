menu = {}
while True:
    try:
        thing = input().upper()
        if thing in menu:
            menu[thing] += 1
        else:
            menu[thing] = 1
    except EOFError:
        # sorted will sort the dictionary alphabetically
        for thing in sorted(menu):
            print(f"{menu[thing]} {thing}")
        break
