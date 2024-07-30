import requests
import sys

def main():
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    value = r.json()['bpi']['USD']['rate_float']
    try:
        time = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
        sys.exit(1)
    if(len(sys.argv) < 2):
        print("Missing command-line argument")
        sys.exit()
    else:
        amount = time * value
        print(f"${amount:,.4f}")

main()
