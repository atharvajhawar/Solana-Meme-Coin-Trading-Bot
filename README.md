# Solana-Meme-Coin-Trading-Bot

This bot scans for newly launched meme coins on Solana, filters them based on specific criteria, and executes trades using the Jupiter Swap API.

Features

Scans new meme coins launching on Solana via DEX Screener & alternative APIs.

Filters tokens based on liquidity and volume.

Executes buy/sell trades using the Jupiter Swap API.

Stores trade history for analysis.

Prerequisites

Before you start, ensure you have the following installed:

Python 3.8+

pip (Python package manager)

PyCharm (Optional but recommended)

Installation

Clone the Repository:

git clone https://github.com/your-repo/solana-meme-bot.git
cd solana-meme-bot

Install Dependencies:

pip install -r requirements.txt

Set Up Environment Variables (Optional)

If needed, configure an .env file with API keys or RPC settings.

Running the Bot

Open PyCharm or any terminal and navigate to the project folder.

Run the bot using:

python main.py

The bot will start scanning for new meme coins and executing trades.

Troubleshooting

No new tokens found? API might be down. Try restarting the bot later.

ImportError? Ensure you have installed dependencies using pip install -r requirements.txt.

Jupiter API errors? Check Jupiter API Status.

Contributing

Feel free to fork the repo, make improvements, and submit pull requests!

License

MIT License

