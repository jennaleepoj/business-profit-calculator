print("=== Business Profit Calculator ===")

cost_price = float(input("Enter cost price per item: R"))
selling_price = float(input("Enter selling price per item: R"))
quantity = int(input("Enter quantity sold: "))

profit_per_item = selling_price - cost_price
total_profit = profit_per_item * quantity
revenue = selling_price * quantity
total_cost = cost_price * quantity

print("\n--- Results ---")
print("Total revenue: R", revenue)
print("Total cost: R", total_cost)
print("Profit per item: R", profit_per_item)
print("Total profit: R", total_profit)

if total_profit >= 2000:
    print("Profit rating: Excellent")
elif total_profit >= 1000:
    print("Profit rating: Good")
elif total_profit > 0:
    print("Profit rating: Low")
elif total_profit == 0:
    print("Profit rating: Break-even")
else:
    print("Profit rating: Loss")