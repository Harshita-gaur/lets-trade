import logging

logger = logging.getLogger(__name__)

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logger.info(
            f"Order Request: {symbol} {side} {order_type} {quantity} {price}"
        )

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        else:
            raise ValueError("Invalid order type")

        logger.info(
            f"Order Response: {order}\n"
            f"{'='*50}"
        )

        return order

    except Exception as e:
        logger.error(f"Order Error: {str(e)}")
        raise