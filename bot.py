import requests

# Corrected API URL
DEX_SCREEN_URL = "https://api.dexscreener.com/latest/dex/search?q=SOL"

BIRDEYE_API = "https://public-api.birdeye.so/defi/tokenlist?sort_by=v24hUSD&sort_type=desc&offset=0&limit=50&min_liquidity=100"
BIRDEYE_HEADERS = {
    "accept": "application/json",
    "x-chain": "solana",
    "X-API-KEY": "b341deff4fdf452ebfab5cb97a013e20"
}

def fetch_new_tokens():
    try:
        response = requests.get(DEX_SCREEN_URL)
        response.raise_for_status()
        data = response.json()
        return data.get("pairs", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching new tokens: {e}")
        return []

def filter_profitable_trades(tokens):
    filtered_tokens = []
    for token in tokens:
        try:
            name = token.get('baseToken', {}).get('name', 'Unknown Token')
            liquidity = token.get('liquidity', {}).get('usd', 0) or 0
            volume = token.get('volume', {}).get('h24', 0) or 0

            print(f"🔍 Checking {name}: Liquidity ${liquidity}, Volume ${volume}")

            if liquidity > 500 and volume > 1000:
                filtered_tokens.append(token)
        except Exception as e:
            print(f" Error filtering token: {e}")
    return filtered_tokens
