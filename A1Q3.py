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
'''
Reference: 
1. CSV File Reading and Writing: https://docs.python.org/3/library/csv.html
2. next() skip header row: https://stackoverflow.com/questions/14257373/how-to-skip-the-headers-when-processing-a-csv-file-using-python
3. array.append() function: https://www.w3schools.com/python/ref_list_append.asp
'''

with open(csv_file, mode='r') as product_inventory:
    product_data = csv.reader(product_inventory)
    # skip header row
    next(product_data)

 # Read over each row in the CSV file
    for row in product_data:
        product_ids.append(int(row[0]))
        product_names.append(row[1])
        categories.append(row[2])
        prices.append(float(row[3]))
        quantity_in_stock.append(int(row[4]))
        suppliers.append(row[5])

# Output the parallel arrays
print("Product IDs:", product_ids)
print("Product Names:", product_names)
print("Categories:", categories)
print("Prices:", prices)
print("Quantity_in_stock:", quantity_in_stock)
print("Suppliers:", suppliers)

