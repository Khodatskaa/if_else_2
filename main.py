price_per_console = float(input("Enter the price of one console box: "))
quantity = int(input("Enter the quantity of consoles: "))
discount_percentage = float(input("Enter the discount percentage (if none, enter 0): "))

print('Choose the operation')
print('1. Count the total cost of the order')
print('2. Count the price of one console including discount')
choice = int(input('Choose the operation number (1/2): '))

if choice == 1:
    total_cost = price_per_console * quantity
    if discount_percentage > 0:
        total_cost -= (discount_percentage / 100) * total_cost
    print(f"Total cost of the order: {total_cost}")
elif choice == 2:
    discounted_price = price_per_console - (discount_percentage / 100) * price_per_console
    print(f"Price of one console including discount: {discounted_price}")
else:
    print()