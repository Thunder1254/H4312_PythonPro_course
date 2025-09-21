result = []

def divider(a, b):
    if a < b:
        raise ValueError("a is smaller than b")
    if b > 100:
        raise IndexError("b is too large")
    return a/b
data = {10: 2, 2: 5, "123": 4, 18: 0, (1, 2): 15, 8 : 4}
for key in data:
    try:
        res = divider(key, data[key])  # fixed kem → key
        result.append(res)
    except ValueError:
        print("ValueError:",key, ' is smaller than b')
    except IndexError:
        print("IndexError:",key,'b is too large')
    except ZeroDivisionError:
        print("ZeroDivisionError:",key,'cannot be divided by 0')
    except TypeError:
        print("TypeError:",key,'can`t be compared')
print(result,'all other ones cant be divided')