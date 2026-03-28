import os
import logging
from binance.client import Client
from dotenv import load_dotenv

logger = logging.getLogger(__name__)

load_dotenv()

def get_client():
    try:
        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("SECRET_KEY")

        if not api_key or not api_secret:
            raise ValueError("API keys not found in environment variables")

        client = Client(api_key, api_secret, testnet=True)

        logger.info("Binance client initialized successfully")

        return client

    except Exception as e:
        logger.error(f"Error initializing client: {str(e)}")
        raise