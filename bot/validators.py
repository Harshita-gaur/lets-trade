def validate_inputs(symbol, side, order_type, quantity, price):
    
    if not symbol:
        raise ValueError("Symbol is required")

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    if order_type == "LIMIT" and price is None:
        raise ValueError("Price is required for LIMIT orders")
    
    estimated_price = price if price else 60000
    if quantity * estimated_price < 100:
        raise ValueError("Order value must be at least 100 USDT")