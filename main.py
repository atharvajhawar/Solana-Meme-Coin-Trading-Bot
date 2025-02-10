import time
from bot import fetch_new_tokens, filter_profitable_trades
from database import save_trade, update_trade, get_open_trades
from trader import execute_trade, sell_token
from price_checker import check_price

TRADE_AMOUNT_SOL = 0.1
PROFIT_TARGET = 1.2


def main():
    while True:
        tokens = fetch_new_tokens()
        if not tokens:
            print("⚠️ No new tokens found. Retrying in 60 seconds...")
            time.sleep(60)
            continue

        profitable_tokens = filter_profitable_trades(tokens)

        for token in profitable_tokens:
            print(f"🟢 Buying {token['baseToken']['name']} ({token['baseToken']['address']})")
            buy_result = execute_trade(token['baseToken']['address'], "buy", TRADE_AMOUNT_SOL)

            if buy_result:
                buy_price = buy_result["price"]
                save_trade(token['baseToken']['name'], token['baseToken']['address'], buy_price)
                print(f"✅ Bought {token['baseToken']['name']} at {buy_price} SOL")


        for trade in get_open_trades():
            name, address, buy_price, _, _ = trade
            current_price = check_price(address)

            if current_price >= buy_price * PROFIT_TARGET:
                print(f"🔴 Selling {name} ({address}) at {current_price} SOL")
                sell_result = sell_token(address, TRADE_AMOUNT_SOL)

                if sell_result:
                    profit = current_price - buy_price
                    update_trade(address, current_price, profit)
                    print(f"💰 Sold {name} with {profit} SOL profit")

        time.sleep(60)


if __name__ == "__main__":
    main()
