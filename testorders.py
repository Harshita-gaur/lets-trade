from bot.logging_config import setup_logging
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_inputs

setup_logging()

client = get_client()

symbol = "BTCUSDT"
side = "BUY"
order_type = "LIMIT"
quantity = 0.002
price = 60000

validate_inputs(symbol, side, order_type, quantity, price)

order = place_order(client, symbol, side, order_type, quantity, price)

print(order)