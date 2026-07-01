# Stock Portfolio Tracker

# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = {}

print("=" * 40)
print("📈 Stock Portfolio Tracker")
print("=" * 40)

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not found!")
        continue

    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity

print("\nYour Portfolio")
print("-" * 40)

total_value = 0

for stock, quantity in portfolio.items():
    value = quantity * stock_prices[stock]
    total_value += value
    print(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${value}")

print("-" * 40)
print(f"💰 Total Portfolio Value = ${total_value}")