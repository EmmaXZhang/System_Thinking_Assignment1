import csv

# Define empty arrays for each column
product_ids = []
product_names = []
categories = []
prices = []
quantity_in_stock = []
suppliers = []

# load data
csv_file = "product_data.csv"

# Read Data into the Program’s Parallel Arrays
with open(csv_file, mode='r') as product_inventory:
    product_data = csv.reader(product_inventory)

    # skip header row
    next(product_data)
