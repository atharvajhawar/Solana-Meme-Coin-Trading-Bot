import requests

JUPITER_SWAP_URL = "https://quote-api.jup.ag/v1/swap"

def execute_trade(token_address, side, amount):
    """Executes a buy or sell order for a given token address."""
    payload = {
        "inputMint": "So11111111111111111111111111111111111111112" if side == "buy" else token_address,
        "outputMint": token_address if side == "buy" else "So11111111111111111111111111111111111111112",
        "amount": amount,
        "slippage": 1,
        "side": side
    }
    try:
        response = requests.post(JUPITER_SWAP_URL, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f" Error executing {side} order: {e}")
        return None

def sell_token(token_address, amount):

    return execute_trade(token_address, "sell", amount)
