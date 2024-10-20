import csv

''' Define global empty arrays for each column '''
product_ids = []
product_names = []
categories = []
prices = []
quantity_in_stock = []
suppliers = []

''' define csv file path'''
csv_file = "product_data.csv"

''' 
Read Data into the Program’s Parallel Arrays
with-> resource management, open()-> open a file, read-only
'''
with open(csv_file, mode='r') as product_inventory:
    product_data = csv.reader(product_inventory)
    ''' skip header row'''
    next(product_data)

    '''Read over each row in the CSV file and append to arrays'''
    for row in product_data:
        product_ids.append(int(row[0]))
        product_names.append(row[1])
        categories.append(row[2])
        prices.append(float(row[3]))
        quantity_in_stock.append(int(row[4]))
        suppliers.append(row[5])

'''Output the parallel arrays'''
print("Product IDs:", product_ids)
print("Product Names:", product_names)
print("Categories:", categories)
print("Prices:", prices)
print("Quantity_in_stock:", quantity_in_stock)
print("Suppliers:", suppliers)

