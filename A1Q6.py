import csv
# global array
product_ids = []
product_names = []
categories = []
prices = []
quantity_in_stock = []
suppliers = []
csv_file = "product_data2.csv"

# load data
def load_record(csv_file):
    product_ids.clear()
    product_names.clear()
    categories.clear()
    prices.clear()
    quantity_in_stock.clear()
    suppliers.clear()

    with open(csv_file, mode='r') as product_inventory:
        product_data = csv.reader(product_inventory)
        # skip header row
        next(product_data)
        # add product detail data to matrix format
        for row in product_data:
            product_ids.append(int(row[0]))
            product_names.append(row[1])
            categories.append(row[2])
            prices.append(float(row[3]))
            quantity_in_stock.append(int(row[4]))
            suppliers.append(row[5])

        print("The record has been loaded successfully!")

# Display current array data
def display_data():
    # load_record(csv_file)
    print(f"{'Product_Id':>10} {'Product_Name':<45} {'Category':<10} {'Price':>10} {'Quantity_in_Stock':>19} {'Supplier':<13}")
    print("-" * 110)
    for i in range(len(product_ids)):
        print(f"{product_ids[i]:>10} {product_names[i]:<45} {categories[i]:<10} {prices[i]:>10.2f} {quantity_in_stock[i]:>19} {suppliers[i]:<13}")



# Add record
def add_data():
    if product_ids:
        new_id = product_ids[-1] + 1
    else:
        new_id = 1001
    product_ids.append(new_id)
    # Collect product details
    product_name = input("Product Name: ")
    category = input("Category: ")
    price = float(input("Price: "))
    stock = int(input("Quantity in Stock: "))
    supplier = input("Supplier: ")


    product_names.append(product_name)
    categories.append(category)
    prices.append(price)
    quantity_in_stock.append(stock)
    suppliers.append(supplier)

    print("The record has been added successfully!")