import csv
'''global array'''
product_ids = []
product_names = []
categories = []
prices = []
quantity_in_stock = []
suppliers = []

'''define csv file'''
csv_file = "product_data2.csv"

'''load data from csv file'''
def load_record(csv_file):
    product_ids.clear()
    product_names.clear()
    categories.clear()
    prices.clear()
    quantity_in_stock.clear()
    suppliers.clear()

    with open(csv_file, mode='r') as product_inventory:
        product_data = csv.reader(product_inventory)
        '''skip header row'''
        next(product_data)
        '''add product detail data to parallel array'''
        for row in product_data:
            product_ids.append(int(row[0]))
            product_names.append(row[1])
            categories.append(row[2])
            prices.append(float(row[3]))
            quantity_in_stock.append(int(row[4]))
            suppliers.append(row[5])

        print("The record has been loaded successfully!")

'''Display current array data - Implement the formatted display'''
def display_data():
    print(f"{'Product_Id':>10} {'Product_Name':<45} {'Category':<10} {'Price':>10} {'Quantity_in_Stock':>19} {'Supplier':<13}")
    print("-" * 110)
    for i in range(len(product_ids)):
        print(f"{product_ids[i]:>10} {product_names[i]:<45} {categories[i]:<10} {prices[i]:>10.2f} {quantity_in_stock[i]:>19} {suppliers[i]:<13}")


'''
Add record function asking the user for each column of information for the new row
process: add record to parallel arrays structure
'''
def add_data():
    if product_ids:
        new_id = product_ids[-1] + 1
    else:
        new_id = 1001
    product_ids.append(new_id)
    '''Collect product details'''
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


'''Delete record from array'''
def delete_data():
    if not product_ids:
        print("No records available to delete.")
        return
    '''else display data'''
    display_data()

    '''check if id exist,
    In a while True loop, the loop itself will run indefinitely until you explicitly break out of it.'''
    while True:
        try:
            delete_id = int(input("Please enter the Product Id to be deleted: "))
            if delete_id in product_ids:
                break
            else:
                print("Product ID not found. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid numeric Product ID.")

    '''find ID, and remove it'''
    delete_index = product_ids.index(delete_id)
    product_ids.pop(delete_index)
    product_names.pop(delete_index)
    categories.pop(delete_index)
    prices.pop(delete_index)
    quantity_in_stock.pop(delete_index)
    suppliers.pop(delete_index)
    print(f"Product with ID {delete_id} deleted successfully.")


'''Save record -> save current array data to csv and load new data to array'''
def save_data():
    with open(csv_file, mode='w', newline='') as product_inventory:
        writer = csv.writer(product_inventory)
        '''write the header:'''
        writer.writerow(
        ["Product ID", "Product Name", "Category", "Price", "Quantity in Stock", "Supplier"])

        '''Write all product data'''
        for i in range(len(product_ids)):
            writer.writerow(
                [product_ids[i], product_names[i], categories[i], prices[i], quantity_in_stock[i], suppliers[i]])

    print("Records saved successfully.")
    '''load new data to array'''
    load_record(csv_file)


'''Exit menu'''
def exit_app():
    print("Exiting the application successfully.")
    exit()


'''Main function'''
def menu():
    while True:
        user_choice = int(input(
           "\nChoose menu option: \n 1.Load records \n 2.Display \n 3.Add record \n 4.Delete record \n 5.Save records \n 6.Exit \n Select: "))
        match user_choice:
            case 1:
                load_record(csv_file)
            case 2:
                display_data()
            case 3:
                add_data()
            case 4:
                delete_data()
            case 5:
                save_data()
            case 6:
                exit_app()
            case _:
                print("Invalid option. Please select from 1 to 6.")


'''Run the menu'''
menu()
