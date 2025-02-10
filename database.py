import sqlite3


conn = sqlite3.connect("trades.db")
cursor = conn.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS trades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    address TEXT,
    buy_price REAL,
    sell_price REAL,
    profit REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()

def save_trade(name, address, buy_price, sell_price=None, profit=None):
    """Save buy/sell trade data to the database."""
    cursor.execute("INSERT INTO trades (name, address, buy_price, sell_price, profit) VALUES (?, ?, ?, ?, ?)",
                   (name, address, buy_price, sell_price, profit))
    conn.commit()

def update_trade(address, sell_price, profit):
    """Update trade with sell price and profit."""
    cursor.execute("UPDATE trades SET sell_price=?, profit=? WHERE address=? AND sell_price IS NULL",
                   (sell_price, profit, address))
    conn.commit()

def get_open_trades():
    """Get all open (unclosed) trades."""
    cursor.execute("SELECT * FROM trades WHERE sell_price IS NULL")
    return cursor.fetchall()
