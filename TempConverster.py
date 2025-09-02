print ("Welcome to the Temperature Converster")
unit_from = 0
def input_type ():
    print ("What would you like to do? \n1. Convert from Celsius \n2. Convert from Fahrenheit \n3. Convert from Kelvin")
    unit_from = input ("Enter your choice (1, 2, or 3) ")
    if unit_from == "1" or unit_from == "2" or unit_from == "3":
       correct_input = "1"
       return unit_from
    else:
        print ("Unrecognized input")
        unit_from = input_type()
        return unit_from
unit_from = input_type()       
unit_too = 0
unit_too_temp = 0
def output_type (unit_from):
    if unit_from == "1":
        print ("What would you like to convert too \n 1. Fahrenheit \n 2. Kelvin")
        unit_too_temp = input ("Enter your choice (1 or 2) ")
        if unit_too_temp == "1":
            unit_too = "2"
            return unit_too
        elif unit_too_temp == "2":
            unit_too = "3"
            return unit_too
        else:
            print ("Unrecognized input")
            unit_too = output_type (unit_from)
            return unit_too        
    elif unit_from == "2":
        print ("What would you like to convert too \n 1. Celsius \n 2. Kelvin")
        unit_too_temp = input ("Enter your choice (1 or 2) ")
        if unit_too_temp == "1":
            unit_too = "1"
            return unit_too
        elif unit_too_temp == "2":
            unit_too = "3"
            return unit_too
        else:
            print ("Unrecognized input")
            unit_too = output_type (unit_from)
            return unit_too
    elif unit_from == "3":
        print ("What would you like to convert too \n 1. Celsius \n 2. Fahrenheit")
        unit_too_temp = input ("Enter your choice (1 or 2) ")
        if unit_too_temp == "1":
            unit_too = "1"
            return unit_too
        elif unit_too_temp == "2":
            unit_too = "2"
            return unit_too
        else:
            print ("Unrecognized input")
            unit_too = output_type (unit_from)
            return unit_too
    else:
        print ("This text should never be displayed")
unit_too = output_type(unit_from)

def c_to_f ():
    pass
def c_to_k ():
    pass
def f_to_c ():
    pass
def f_to_k ():
    pass
def k_to_c ():
    pass
def k_to_f ():
    pass