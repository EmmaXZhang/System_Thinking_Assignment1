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

