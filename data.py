"""
Actual database is created in this module
"""

products=[] # temporary database

def add_product(product_name,product_price):
    product_record={"name":product_name,"price":product_price}
    products.append(product_record)

def delete_product(product_name):
    for each_record in products:
        if each_record["name"]==product_name:
            print(f"{each_record} has been removed")
            products.remove(each_record)

def display_products():
    return products

