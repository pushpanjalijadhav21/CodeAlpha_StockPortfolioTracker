print("===== Stock Portfolio Tracker =====")

stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
}

portfolio = {}
total_investment = 0

while True:
    print("\nAvailable Stocks:")
    for stock, price in stock_prices.items():
        print(f"{stock} : {price}")

    stock_name = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Invalid stock name! Please try again.")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Quantity must be greater than 0.")
        continue

    portfolio[stock_name] = quantity
    total_investment += stock_prices[stock_name] * quantity

print("\n========== Portfolio Summary ==========")

if portfolio:
    for stock, quantity in portfolio.items():
        price = stock_prices[stock]
        print(f"{stock} : {quantity} x {price} = {quantity * price}")

    print("--------------------------------------")
    print(f"Total Investment = {total_investment}")
else:
    print("No stocks purchased.")

