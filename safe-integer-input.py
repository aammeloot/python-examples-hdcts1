def safe_integer_input(message, low_boundary, high_boundary):
    result = 0
    input_valid = False
    while not input_valid:
        try:
            result = int(input(message))
            if result >= low_boundary and result <= high_boundary:
                input_valid = True
            else:
                print("Out of boundaries")
        except:
            TypeError
            print("Make sure you enter a numerical value")
    return result
