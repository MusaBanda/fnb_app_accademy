food = []
prices = []
total = 0

while True:
    item = input("Enter food item (or 'done' to finish): ")
    if item.lower() == 'done':
        break
    else:
        price = float(input(f"Enter price for {item}: "))
        food.append(item)
        prices.append(price)

print("\nYour Cart:")
for i in range(len(food)):
    print(f"{food[i]} - R{prices[i]:.2f}")
    total += prices[i]

print(f"\nYour total: R{total:.2f}")
