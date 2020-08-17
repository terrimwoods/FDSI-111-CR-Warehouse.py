"""
    Program: Warehouse Management System
        Author: Terri Woods
Description:    
    1 - Register a new item
        id (auto generated)
        title (str)
        category (str)
        price (float)
        stock (int)

    2 - Display Catalog
    3 - Update stock
    4 - Remove item from catalog
    5 - Print Total stock value
    6 - Out of stock

"""
#imports
from menu import clear, print_menu, print_header, print_item
from item import Item #from file import class
import pickle

# Serialize the objects

# global vars
catalog = []
data_file = "warehouse.data"
last_id = 1

def serialize_catalog():
    global data_file #points back to the global to get the def of the variable
    writer = open(data_file, "wb") # create/open a file to write binary
    pickle.dump(catalog, writer)
    writer.close() # close the stream, released the file
    print("**Data serialized!")

def deserialize_catalog():
    try:
        global data_file
        global last_id
        reader = open(data_file, "rb") # open file to read binary
        temp_list = pickle.load(reader)

        for item in temp_list:
            catalog.append(item)

        last_item = catalog[-1]
        last_id = last_item.id + 1

        print("*** Deserialized " + str( len(catalog))+ "items" )

    except:
        print("Error, could not load data")

#fn
def register_item():
    global last_id
    try:
        print_header("Register New Item")
        title = input('Please provide a title:  ')
        cat = input('Please provide the category: ')
        price = float(input('Please provide a price: '))
        stock = int(input('Please provide the stock: '))

        id = last_id
        last_id += 1
        

        item = Item(id, title, cat, price, stock)
        catalog.append(item)

        #item.id = id
        #item.title = title
        #item.category = cat
        #item.price = price
        #item.stock = stock

        how_many = len(catalog)
        print('You now have:' + str(how_many) + " item on the catalog")
    except ValueError:
        print("Error: incorrect value, try again")
    except:
        print("Error, this is not a float")

def update_stock():
    # show catalog to the user
    # ask to choose one id
    # search for the item with that id
    # ask for the new item stock value
    # set the stock value
    try:
        display_catalog()
        id = input("Please provide the Item id: ")
        found = False
        for item in catalog:
            if (str(item.id) == id):
                found = True
                val = input("Please provide new stock value: ")
                item.stock = int(val)
                print("Stock value has been updated")
        if(not found):
            print("**Error:  Invalid ID, verify and try again!")  

    except ValueError:
        print("**Invalid number:  verify and try again")    
    except: 
        print("Error, something went wrong")
def update_price():
    try:
        display_catalog()
        id = input("Please provide the Item ID: ")
        found = False
        for item in catalog:
            if(str(item.id) == id):
                found = True
                val = input("Please update new price: ")
                item.price = float(val)
                print("Price has been updated")
        if(not found):
            print("**Error: Invalid ID, verify and try again")  

    except ValueError:
        print("**Invalid number:  verify and try again")    
    except: 
        print("Error, something went wrong")              

def display_catalog():
    print_header("Your Current Catalog")
    # travel the list
    # print the title
    for item in catalog:
     print_item(item)

def delete_item():
    # delete stock items 
  
    try:
        display_catalog()
        id = input("Please provide the Item ID: ")
        found = False
        for item in catalog:
            if(str(item.id) == id):
                found = True
                del item.id, item.title, item.category, item.price, item.stock
                print("Item has been deleted")
        if(not found):
            print("**Error: Invalid ID, verify and try again")  

    except ValueError:
        print("**Invalid number:  verify and try again")    
    except: 
        print("Error, something went wrong")

        
def display_out_of_stock():
    print_header("Items currently out of stock")
    for item in catalog:
        if(item.stock == 0):
            print (item.title + "|" + str(item.stock))

def total_stock_value():
    total = 0.0
    for item in catalog:
        total += item.price * item.stock
    print("Total value:" + str(total))

def list_of_categories(): # list the items in the catalog without duplicating them
    global catalog
    print_header("List of categories: ")   
          
    catalog = []
    [catalog.append(cat) for item in catalog if item not in catalog] 
  
    how_many = len(catalog)
    print("You now have: " + str(how_many) + "categories")
   





# instructions

deserialize_catalog()

input("Press Enter to continue")

opc=''
while(opc != 'x'): 
    clear()
    print_menu()

    opc = input('Please choose an option:')

    # if comparison  
    if(opc == '1'):
        register_item()
        serialize_catalog()
    elif(opc == '2'):
        display_catalog()
    elif(opc == '3'):
        update_stock()
        serialize_catalog()
    elif(opc == '4'): 
        update_price()
        serialize_catalog() 
    elif(opc == '5'):
        delete_item()
        serialize_catalog()
    elif(opc == '6'):
        display_out_of_stock()
    elif(opc == '7'):
        total_stock_value()
    elif(opc == "8"):
        list_of_categories()

    input('Press enter to continue.....')



