import math
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
starttemp = 0
endtemp = 0
def selector (unit_from, unit_too):
    if unit_from == "1" and unit_too == "2":
        c_to_f()
        pass
    if unit_from == "1" and unit_too == "3":
        c_to_k()
        pass
    if unit_from == "2" and unit_too == "1":
        f_to_c()
        pass
    if unit_from == "2" and unit_too == "3":
        f_to_k()
        pass
    if unit_from == "3" and unit_too == "1":
        k_to_c()
        pass
    if unit_from == "3" and unit_too == "2":
        k_to_f()
        pass
    pass
def ender ():
    again = input ("Would you like to convert again? (Y or N) ")
    if again == "Y":
        unit_from = input_type()
        unit_too = output_type(unit_from)
        selector (unit_from, unit_too)
    elif again == "N":
        print ("Bye Bye")
        pass
    else:
        print ("Invalid input recognized")
        ender ()
def float_test (starttemp):
    try:
        float(starttemp)
        return True
    except ValueError: 
        return False
def c_to_f ():
    starttemp = input("""Please type your temperature in Celsius (no units) """)
    if float_test(starttemp):
        starttemp = float(starttemp)
        endtemp = starttemp * 9/5 + 32
        print (f"Your temperature in Fahrenheit is {round(endtemp,2)} degrees")
        ender()
    else:
        print ("Invalid Input, please try again")
        c_to_f()
def c_to_k ():
    starttemp = input("""Please type your temperature in Celsius (no units) """)
    if float_test(starttemp):
        starttemp = float(starttemp)
        endtemp = starttemp + 273.15
        print (f"Your temperature in Kelvin is {round(endtemp,2)} degrees")
        ender()
    else:
        print ("Invalid Input, please try again")
        c_to_k()
def f_to_c ():
    starttemp = input("""Please type your temperature in Fahrenheit (no units) """)
    if float_test(starttemp):
        starttemp = float(starttemp)
        endtemp = (starttemp - 32) * 5/9
        print (f"Your temperature in Celsius is {round(endtemp,2)} degrees")
        ender()
    else:
        print ("Invalid Input, please try again")
        f_to_c()
def f_to_k ():
    starttemp = input("""Please type your temperature in Fahrenheit (no units) """)
    if float_test(starttemp):
        starttemp = float(starttemp)
        endtemp = (starttemp -32) * 5/9 + 273.15
        print (f"Your temperature in Kelvin is {round(endtemp,2)} degrees")
        ender()
    else:
        print ("Invalid Input, please try again")
        f_to_k()
def k_to_c ():
    starttemp = input("""Please type your temperature in Kelvin (no units) """)
    if float_test(starttemp):
        starttemp = float(starttemp)    
        endtemp = starttemp - 273.15
        print (f"Your temperature in Celsius is {round(endtemp,2)} degrees")
        ender()
    else:
        print ("Invalid Input, please try again")
        k_to_c()
def k_to_f ():
    starttemp = input("""Please type your temperature in Kelvin (no units) """)
    if float_test(starttemp):
        starttemp = float(starttemp)
        endtemp = (starttemp - 273.15) * 9/5 + 32
        print (f"Your temperature in Fahrenheit is {round(endtemp,2)} degrees")
        ender()
    else:
        print ("Invalid Input, please try again")
        k_to_f()
selector (unit_from, unit_too)
