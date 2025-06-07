# Portfolio Manager

This repository contains a simple command line program to manage an investment portfolio.

## Usage

Run the script with Python and one of the available commands:

```bash
python3 portfolio.py add SYMBOL QUANTITY PRICE  # Add or update an asset
python3 portfolio.py remove SYMBOL              # Remove an asset
python3 portfolio.py list                       # List all assets
python3 portfolio.py total                      # Show total portfolio value
```

The program stores its data in `portfolio.json` in the current directory.
