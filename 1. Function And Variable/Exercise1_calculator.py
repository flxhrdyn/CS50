def calc():
    print("Simple Calculator")
    print("-----------------") 
    x = float(input("What's X? ")) # input x
    y = float(input("What's Y? ")) # input y

    print("Calculating......")
    print("-----------------") 
    add(x, y) # calling function add
    sub(x, y) # calling function sub
    div(x, y) # calling function div
    mul(x, y) # calling function mul

def add(x, y): # function for addition
    print(f"The Addition of X & Y is", x + y)

def sub(x, y): # function for subtraction
    print(f"The subtraction of X & Y is", x - y)

def mul(x, y): # function for multiplication
    print(f"The multiplication of X & Y is", x * y)

def div(x, y): # function for division
    print(f"The multiplication of X & Y is", x / y)

calc() # calling calc function


# print("Simple Calculator")
# print("-----------------")
# x = float(input("What's X? ")) # input x
# y = float(input("What's Y? ")) # input y

# add = x + y 
# sub = x - y
# mul = x * y
# div = x / y

# print("Calculating......")
# print("-----------------")
# print(f"The Addition of X & Y is {add}")
# print(f"The Subtraction of X & Y is {sub}")
# print(f"The Multiplication of X & Y is {mul}")
# print(f"The Division of X & Y is {div}")
