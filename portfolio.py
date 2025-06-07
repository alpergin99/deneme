import argparse
import json
from pathlib import Path

PORTFOLIO_FILE = Path('portfolio.json')

def load_portfolio():
    if PORTFOLIO_FILE.exists():
        with PORTFOLIO_FILE.open('r') as f:
            return json.load(f)
    return {}

def save_portfolio(data):
    with PORTFOLIO_FILE.open('w') as f:
        json.dump(data, f, indent=2)

def add_asset(symbol, quantity, price):
    data = load_portfolio()
    data[symbol] = {'quantity': quantity, 'price': price}
    save_portfolio(data)
    print(f"Added {symbol}: {quantity} @ {price}")

def remove_asset(symbol):
    data = load_portfolio()
    if symbol in data:
        del data[symbol]
        save_portfolio(data)
        print(f"Removed {symbol}")
    else:
        print(f"{symbol} not found")

def list_assets():
    data = load_portfolio()
    if not data:
        print("Portfolio is empty")
        return
    for sym, info in data.items():
        q = info['quantity']
        p = info['price']
        print(f"{sym}: {q} @ {p} each")

def total_value():
    data = load_portfolio()
    total = sum(info['quantity'] * info['price'] for info in data.values())
    print(f"Total value: {total}")

def main():
    parser = argparse.ArgumentParser(description='Simple portfolio manager')
    sub = parser.add_subparsers(dest='command')

    add = sub.add_parser('add', help='Add or update asset')
    add.add_argument('symbol')
    add.add_argument('quantity', type=float)
    add.add_argument('price', type=float)

    remove = sub.add_parser('remove', help='Remove asset')
    remove.add_argument('symbol')

    sub.add_parser('list', help='List portfolio')
    sub.add_parser('total', help='Show total value')

    args = parser.parse_args()
    if args.command == 'add':
        add_asset(args.symbol, args.quantity, args.price)
    elif args.command == 'remove':
        remove_asset(args.symbol)
    elif args.command == 'list':
        list_assets()
    elif args.command == 'total':
        total_value()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
