menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0
while True:
    try:
    # title will capitalize every first letter of the vocabulary
        dish = input("Item: ").title()
        if dish in menu:
            total += menu[dish]
            print(f"Total: ${total:.2f}")
            continue
    except EOFError:
        print()
        break

