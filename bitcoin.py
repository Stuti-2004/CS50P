import requests
import sys

try:
    if (len(sys.argv) > 1):
        if(float(sys.argv[1]) or int(sys.argv[1])):
            #print(sys.argv[1])

            response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            #print(json.dumps(response.json(), indent = 2))

            o = response.json()
            rate = (o['bpi']['USD']['rate']).replace(",", "")
            price = float(rate) * float(sys.argv[1])
            print(f"${price:,.4f}")

        else:
            print("Command-line argument is not a number")
            sys.exit(1)
    else:
        print("Missing command-line argument")
        sys.exit(1)

except (requests.RequestException, KeyError):
    print("error")
    sys.exit(1)