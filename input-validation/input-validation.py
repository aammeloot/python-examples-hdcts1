# Demonstration of input validation
# Creating a menu

def display_menu():
    print("Welcome to Fife College café.")
    print("1 - Coffee")
    print("2 - Tea")
    print("3 - Hot Chocolate")
    
def main():
    
    hot_drink = 0 # Variable hot drink, integer
    # Displaying the menu
    display_menu()
    hot_drink = int(input("Please make a selection: "))
    # While input is invalid, ask again
    while hot_drink < 1 or hot_drink > 3:
        # Displaying the menu
        display_menu()
        hot_drink = int(input("Please make a selection: "))
    
if __name__ == "__main__":
    main()
    
