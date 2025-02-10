import sqlite3

conn = sqlite3.connect("trades.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM trades")
trades = cursor.fetchall()

print("\n Trade History:")
for trade in trades:
    print(f"🔹 {trade[1]} | Buy: {trade[3]} SOL | Sell: {trade[4]} SOL | Profit: {trade[5]} SOL")

conn.close()
