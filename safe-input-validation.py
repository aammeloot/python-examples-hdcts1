# We need to enter a number between 1 and 10
# 2 issues: If we do not enter a number, it crashes
# second issue: validate the input values

# This is a flag that will be used for input validation
valid = False

while not valid:
    # Enter the choice, which is a string
    choice = input("Enter a number between 1 and 10")
    # First test, only move on if the string is only
    # constituted of numbers (this avoids a crash)
    if choice.isnumeric():
        # in that case it is safe to convert choice
        # to an integer
        choice = int(choice)
        if choice >= 1 and choice <= 10:
            valid = True
        else:
            print("Error: value not between 1 and 10")
    else:
        print("Error: value not numeric")

