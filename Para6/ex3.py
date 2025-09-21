def checker(var1):
    if type(var1) != str:
        raise TypeError(f"Sorry we can`t work with {type(var1)} this variable needs to be str")
    else:
        return var1

first_var = 1432524
checker(first_var)


