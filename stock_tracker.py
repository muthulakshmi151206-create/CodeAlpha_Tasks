stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "AMZN": 130,
    "META": 300
}

print("📈 Stock Portfolio Tracker")

total = 0
portfolio = {}

while True:
    stock = input("Enter stock name (or 'stop'): ").upper()

    if stock == "STOP":
        break

    if stock not in stock_prices:
        print("Stock not found!")
        continue

    qty = int(input("Enter quantity: "))
    portfolio[stock] = qty
    total += stock_prices[stock] * qty

print("\nYour Portfolio:")
for s, q in portfolio.items():
    print(f"{s} - {q} shares")

print("\nTotal Investment Value:", total)

# Save to file
with open("portfolio_result.txt", "w") as f:
    f.write("Stock Portfolio Result:\n")
    for s, q in portfolio.items():
        f.write(f"{s}: {q} shares\n")
    f.write(f"\nTotal Investment: {total}")

print("\nSaved to portfolio_result.txt")
