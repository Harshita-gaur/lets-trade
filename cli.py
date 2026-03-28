import argparse
from bot.logging_config import setup_logging
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_inputs

def main():
    # setup logging
    setup_logging()

    parser = argparse.ArgumentParser(description="Trading Bot CLI")

    parser.add_argument("--symbol", required=True, help="Trading pair (e.g., BTCUSDT)")
    parser.add_argument("--side", required=True, help="BUY or SELL")
    parser.add_argument("--type", required=True, help="MARKET or LIMIT")
    parser.add_argument("--quantity", type=float, required=True, help="Order quantity")
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")

    args = parser.parse_args()

    try:
        # validate inputs
        validate_inputs(args.symbol, args.side, args.type, args.quantity, args.price)

        # get client
        client = get_client()

        # print request summary
        print("\n📤 Order Request:")
        print(vars(args))

        # place order
        order = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        # print response
        print("\n✅ Order Response:")
        print({
            "orderId": order.get("orderId"),
            "type": order.get("type"),
            "status": order.get("status"),
            "executedQty": order.get("executedQty"),
            "avgPrice": order.get("avgPrice")
        })

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")


if __name__ == "__main__":
    main()