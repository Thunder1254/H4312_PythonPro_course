class WrongSizeError(Exception):
    def __str__(self):
        return f"You put in the wrong sizes for the construction project"

def checker(var1):
    if first_var >= second_var:
        if type(var1) == int:
            pass
        else:
            raise TypeError(f"Sorry we can`t work with {type(var1)} this variable needs to be int or more than zero")


try:
    first_var = int(input("Put in the length for the material here:   "))
    second_var = int(input("Put in the width for the material here:   "))
    final_dimentions = first_var/second_var
    print(final_dimentions)
    checker(first_var)
    checker(second_var)
except ZeroDivisionError:
    print("The material size needs to be more that zero")
except TypeError:
    print("The material size needs to be in numbers")





