import sys
import json
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
    
try:
    bitcoins = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    r = requests.get('https://rest.coincap.io/v3/assets/bitcoin',params={'apiKey': '58ca4e56b5521b05405621cf220e0ddaba341324e9ffba0970706c150b3ce9af'})
    r.raise_for_status()
    
    data = r.json()
    price = float(data["data"]["priceUsd"])

    total = bitcoins * price
    print(f"${total:,.4f}")
    
except requests.RequestException:
    sys.exit("Failed to fetch Bitcoin price")
except (KeyError,ValueError):
    sys.exit("Failed to parse API response")