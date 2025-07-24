from dotenv import load_dotenv
import os
from binance.client import Client

load_dotenv()
api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_API_SECRET")

client = Client(api_key, api_secret)

try:
    account = client.get_account()
    print("Connexion réussie ! Solde disponible :")
    for balance in account['balances']:
        if float(balance['free']) > 0:
            print(balance)
except Exception as e:
    print("Erreur de connexion :", e)
