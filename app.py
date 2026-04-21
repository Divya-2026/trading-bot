import argparse
import logging
import random

logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def validate_input(symbol, side, order_type, quantity, price):
    if not symbol.endswith("USDT"):
        raise ValueError("Symbol must end with USDT")

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Type must be MARKET or LIMIT")

    if quantity <= 0:
        raise ValueError("Quantity must be > 0")

    if order_type == "LIMIT" and price is None:
        raise ValueError("LIMIT order needs price")

def place_order(symbol, side, order_type, quantity, price):
    logging.info(f"Order Request: {symbol}, {side}, {order_type}, {quantity}, {price}")

    response = {
        "orderId": random.randint(100000, 999999),
        "status": "FILLED",
        "executedQty": quantity,
        "avgPrice": price if price else "market_price"
    }

    logging.info(f"Order Response: {response}")
    return response

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_input(args.symbol, args.side, args.type, args.quantity, args.price)

        print("\nOrder Request:")
        print(vars(args))

        response = place_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\nOrder Response:")
        print(response)

        print("\nOrder placed successfully!")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()