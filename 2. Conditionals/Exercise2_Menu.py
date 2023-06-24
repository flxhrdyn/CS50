# buat program menu restoran
# bisa pilih menu dan keluar harganya
# jika jumlah pesanan genap maka akan ada diskon 50%

# to-do cari cara supaya food*quantity

def menu(): # menu function which will print out the menu list
    
    print("========Restaurant Menu========")
    print("1. Fried Rice Rp 15.000 \n2. Shrimp Tempura Rp 10.000 \n3. Dimsum Rp 5.000")
    print("===============================")
    print("50% DISCOUNT IF YOU BUY A SAME MENU TWICE!\n")

menu() # calls menu function

def main(): # main function
    choice = int(input("Which menu do you want to buy? ")) # this is choice variable
    quantity = int(input("How much? ")) # this is a quantity variable

    if choice == 1: # if the user choose menu 1, the following code will run
        price = float(15000) # the price for The Fried Rice
        discount = float(price*0.5) # the 50% discount calculation

        if isEven(quantity): # if the quantity is even then the menu is going to be discounted, quantity is the argument
            total = round(quantity*(price - discount)) # total if the menu gets discounted
            print(f"\nYou Get a 50% Discount! \nThe Total Bill is Rp {total}") # print the total bill

        else: # if the quantity is not even the normal price will be applied
            total = round(price * quantity) # total with normal price
            print(f"The Total Bill is Rp {total}") # print the total bill

    elif choice == 2: # if the user choose menu 2, the following code will run
        price = float(10000) # the price for The Shrimp Tempura
        discount = float(price*0.5)
        if isEven(quantity):
            total = round(quantity*(price - discount))
            print(f"\nYou Get a 50% Discount! \nThe Total Bill is Rp {total}")
        else:
            total = round(price * quantity)
            print(f"The Total Bill is Rp {total}")

    elif choice == 3: # if the user choose menu 3, the following code will run
        price = float(5000) # the price for The Dimsum
        discount = float(price*0.5)
        if isEven(quantity):
            total = round(quantity*(price - discount))
            print(f"\nYou Get a 50% Discount! \nThe Total Bill is Rp {total}")
        else:
            total = round(price * quantity)
            print(f"The Total Bill is Rp {total}")

    else: # if the user doesn't choose either menu 1, 2, or 3 the following code will run
        print("This Menu is Unavailable")


def isEven(evnum): # function to check whether a number is even or not, ev num is the parameter
    return evnum % 2 == 0 # even number will have a modulus of 0 if divided by 2

main() # calls main function