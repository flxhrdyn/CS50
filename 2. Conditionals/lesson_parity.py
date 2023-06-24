def main():
    x = int(input("Enter a Number : ")) 

    if isEven(x): # if x is even
        print("This Number is Even")
    else: # if x is not even (odd)
        print("This Number is Odd")

def isEven(n): # this function will check whether the number we've input is even or not
    return n % 2 == 0 # return true if the modulus of n equals to 0 (even) if not return false (odd)

    # or if you like to over complicate things you can use this instead:
    # if n % 2 == 0: # if the modulus of n equals to 0, the number is even
    #     return True # retun true if the statement is true 
    # else: # if the modulus of n not equals to 0 
    #     return False # retun false if the statement is false
    
main() # calls the main function

