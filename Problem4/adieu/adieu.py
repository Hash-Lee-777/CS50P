# learn to surf the document
import inflect

def main():
    p = inflect.engine()
    name = []
    try:
        while True:
            name.append(input("Name: "))
    except EOFError:
        print(f"Adieu, adieu, to {p.join(name)}")

main()


