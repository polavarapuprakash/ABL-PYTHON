products = ["Laptop", "Mouse", "Keyboard"]
stock = [10, 20, 15]
price = [40000, 500, 1000]

orders = [
    [0, 2],   # 2 laptops
    [1, 5],   # 5 mice
    [2, 3]    # 3 keyboards
]

discount = 10
revenue = 0

print("E-Commerce Order Report")

for order in orders:
    product_id, quantity = order

    if quantity <= stock[product_id]:
        amount = price[product_id] * quantity
        final_amount = amount - amount * discount / 100

        revenue += final_amount
        stock[product_id] -= quantity

        print(products[product_id],
              "Quantity:", quantity,
              "Bill:", final_amount)
    else:
        print("Insufficient stock:", products[product_id])

# Process one customer return
return_product = 1
return_quantity = 2

stock[return_product] += return_quantity
revenue -= price[return_product] * return_quantity * (1 - discount / 100)

print("\nFinal Revenue:", revenue)
print("Final Inventory:")

for i in range(len(products)):
    print(products[i], "Stock:", stock[i])