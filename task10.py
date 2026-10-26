# Warehouse Inventory Reconciliation

num_products = int(input("Enter number of products: "))

REORDER_LEVEL = 100

print("\n===== WAREHOUSE INVENTORY REPORT =====")

for i in range(num_products):

    print(f"\nProduct {i+1}")

    product_name = input("Enter Product Name: ")

    opening_stock = int(input("Enter Opening Stock: "))
    incoming_stock = int(input("Enter Incoming Quantity: "))
    dispatched_stock = int(input("Enter Dispatched Quantity: "))
    closing_stock = int(input("Enter Actual Closing Stock: "))

    # Expected Closing Stock
    expected_closing = (
        opening_stock +
        incoming_stock -
        dispatched_stock
    )

    # Discrepancy
    discrepancy = closing_stock - expected_closing

    # Replenishment Requirement
    if closing_stock < REORDER_LEVEL:
        replenishment = REORDER_LEVEL - closing_stock
    else:
        replenishment = 0

    print("\n----- Reconciliation Summary -----")
    print(f"Product Name          : {product_name}")
    print(f"Opening Stock         : {opening_stock}")
    print(f"Incoming Quantity     : {incoming_stock}")
    print(f"Dispatched Quantity   : {dispatched_stock}")
    print(f"Expected Closing      : {expected_closing}")
    print(f"Actual Closing        : {closing_stock}")

    if discrepancy == 0:
        print("Status                : No Discrepancy")
    elif discrepancy > 0:
        print(f"Excess Stock          : {discrepancy}")
    else:
        print(f"Stock Shortage        : {-discrepancy}")

    print(f"Replenishment Needed  : {replenishment}")

print("\n===== RECONCILIATION COMPLETED =====")
