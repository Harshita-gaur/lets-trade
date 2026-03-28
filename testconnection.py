from binance.client import Client
import os
from dotenv import load_dotenv

load_dotenv()

client=Client(
    os.getenv("API_KEY"),
    os.getenv("SECRET_KEY"),
    testnet=True
)
client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
balance = client.futures_account_balance()
print(balance)