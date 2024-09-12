import csv
# global array
product_ids = []
product_names = []
categories = []
prices = []
quantity_in_stock = []
suppliers = []

# load data
csv_file = "product_data.csv"


# with-> resource management, open()-> open a file, read-only
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

# print product inventory data in format
def display_data():
    print(f"{'Product_Id':>10} {'Product_Name':<45} {'Category':<10} {'Price':>10} {'Quantity_in_Stock':>19} {'Supplier':<13}")
    print("-" * 110)
    for i in range(len(product_ids)):
        print(f"{product_ids[i]:>10} {product_names[i]:<45} {categories[i]:<10} {prices[i]:>10.2f} {quantity_in_stock[i]:>19} {suppliers[i]:<13}")
