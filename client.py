"""
This is client code to handle product information
"""
import data

def user_add_product():
    product_name=input("Enter product name ")
    product_price=int(input("Enter price "))
    data.add_product(product_name,product_price)

def user_delete_product():
    product_name=input("Enter the product to remove ")
    data.delete_product(product_name)

def user_search_product():
    all_products=data.display_products()
    product_name=input("Enter the product name to search ")
    count_records=0
    for each_product in all_products:
        if product_name == each_product["name"]:
            print(f"{product_name} is present in database!")
            break
        count_records+=1
    if len(all_products) == count_records:
        print(f"{product_name} is not present")

def user_display_products():
    all_products=data.display_products()
    for each_product in all_products:
        print(each_product["name"],each_product["price"])

select_choice="""
1. Add product
2. Delete product
3. Search product
4. Display products
5. Quit
"""

def menu():
    choice=int(input(select_choice))
    while choice!=5:
        if choice==1:
            user_add_product()
        elif choice==2:
            user_delete_product()
        elif choice==3:
            user_search_product()
        elif choice==4:
            user_display_products()
        else:
            break
        choice=int(input(select_choice))

menu()  # call menu function
