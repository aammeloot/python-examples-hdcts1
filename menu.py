#Demonstration of input validation
#Creating a menu

def display_menu():
    print("Welcome to Fife College cafe.")
    print("1 - Coffee")
    print("2 - Tea")
    print("3 - Hot Chocolate")
    
def coffee():
    print("You have chosen Coffee")
    
def tea():
    print("You have chosen Tea")
    
def hot_chocolate():
    print("You have chosen Hot Chocolate")

# Main program, diplays a menu and offers three choices
def main():
    
    hot_drink = 0 # Variable hot drink, integer
    
    # Displaying the menu
    display_menu()
    # Make sure it is type safe:
    # 
    hot_drink = input("Please make a selection: ")



    while not hot_drink.isnumeric() or ()



    # While the input is invalid, ask again
    while hot_drink < 1 or hot_drink > 3:
       display_menu()
       hot_drink = int(input("Please make a selection: "))
           
    if hot_drink == 1:
        coffee()
    elif hot_drink == 2:
        tea()
    elif hot_drink == 3:
        hotChocolate()

if __name__ == "__main__":
    main()