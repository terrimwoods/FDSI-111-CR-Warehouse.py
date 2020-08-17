import os
import datetime
def print_menu():
    print("-"*36)
    print(" Warehouse mgn sys      ["+ get_time() +"] ")
    print("-" * 36)

    print("[1] Register New Item")
    print("[2] Display Catalog")
    print("[3] Update Stock")
    print("[4] Update the Price")
    print("[5] Delete Item")
    print("[6] Display out of stock items")
    print("[7] Total stock value") # sum of all items (price * stock)
    print("[8] List of catagories") # different cats (do not duplicate)
    print("[x] Close")

def print_header(title):
    clear()
    print('-' * 80)
    print(title)
    print('-' * 80)

def print_item(item):
    print(
            str(item.id).rjust(3)
            + " | " + item.title.ljust(25) 
            + " | " + item.category.ljust(12) 
            + " | " + str(item.stock).rjust(11)
            + " | $" + str(item.price).rjust(15)
        )
    print("-" *80)

def get_time():
    now = datetime.datetime.now()
    return now.strftime("%a %H:%M")

def clear():
    return os.system('cls' if os.name == 'nt' else 'clear')
