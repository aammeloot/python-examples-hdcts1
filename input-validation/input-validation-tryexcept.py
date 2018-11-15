# Demonstration of input validation
# This time with exception handling
# Creating a menu

def display_menu():
    print("Welcome to Fife College café.")
    print("1 - Coffee")
    print("2 - Tea")
    print("3 - Hot Chocolate")
    
def main():
    
    hot_drink = 0 # Variable hot drink, integer
    input_valid = False # Input validation condition
    
    # Repeat while input is invalide
    while not input_valid: 
        display_menu() 
        try: # Trying to convert input to integer
            hot_drink = int(input("Please make a selection: "))
            if hot_drink >= 1 and hot_drink <=3:
                input_valid = True # In the boundaries
            else: # Out of the boundaries
                print("Your number needs to be between 1 and 3")
        except: # Handle if text was typed in by user
            TypeError
            print("You need to enter an actual number")

    
if __name__ == "__main__":
    main()
    

