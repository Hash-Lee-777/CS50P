def main():
    sum = 50
    while sum > 0:
        print("Amount Due:", sum)
        insert = int(input("Insert Coin: "))
        # notice using and
        if(insert != 5 and insert != 10 and insert != 25):
            continue
        sum -= insert
        if sum > 0:
            continue
        else:
            break
    print("Change Owed:", - sum)
main()
