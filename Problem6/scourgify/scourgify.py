import sys
import csv

def main():
    if len(sys.argv) != 3:
        sys.exit("Invalid arguments.")
    try:
        with open(sys.argv[1]) as input, open(sys.argv[2], "w", newline="") as output:
            reader = csv.DictReader(input)
            writer = csv.DictWriter(output, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                lastname, firstname = row["name"].strip().split(", ")
                writer.writerow({"first": firstname, "last": lastname, "house": row["house"]})

    except FileNotFoundError:
        sys.exit("File does not exist.")

main()
