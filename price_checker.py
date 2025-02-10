import requests

BIRDEYE_PRICE_API = "https://api.birdeye.so/public/price"
BIRDEYE_HEADERS = {"X-API-KEY": "b341deff4fdf452ebfab5cb97a013e20"}  # Replace with your key

def check_price(token_address):

    try:
        response = requests.get(f"{BIRDEYE_PRICE_API}?address={token_address}", headers=BIRDEYE_HEADERS)
        response.raise_for_status()
        data = response.json()
        return data.get("data", {}).get("value", 0)
    except requests.exceptions.RequestException as e:
        print(f"❌ Error fetching token price: {e}")
        return 0
