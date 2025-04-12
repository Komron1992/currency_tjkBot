💱 Currency Rates Telegram Bot for Tajik Banks 🇹🇯
This is a Telegram bot that displays up-to-date currency exchange rates from various banks in Tajikistan.
Users can easily view rates for USD, EUR, RUB, and CNY — either from all banks at once or by choosing a specific bank using built-in message buttons.

📌 Features
View exchange rates from:

Amonatbonk

Eskhata

Arvand

Imon

Orionbonk

Easy-to-use message reply buttons

/start command to initialize the bot

Real-time data fetched from a custom API (/api/currencies/)

Built with python-telegram-bot (v20+)

Fully asynchronous and optimized for performance

🛠 Tech Stack
Python 3.10+

python-telegram-bot

asyncio

requests

FastAPI (for the backend API — not included here)

▶️ How to Run
Clone the repo:

git clone https://github.com/Komron1992/currency-tjbot.git
cd currency-tjbot
Install dependencies:

pip install -r requirements.txt
Create a .env file and add your bot token:

TELEGRAM_TOKEN=your_telegram_bot_token
Make sure your backend API is running at:

http://127.0.0.1:8000/api/currencies/
Run the bot:

python currency_tjbot.py
📷 Screenshots

✨ Example Usage

/start

👉 Choose a bank from the menu:
- All Banks
- Eskhata
- Amonatbonk
...

💱 Bot replies with:
USD:
Buy: 10.82
Sell: 10.92
Source: Eskhata
...
📬 Contact
Created by Komron1992
If you like this project, please ⭐️ it and feel free to contribute!