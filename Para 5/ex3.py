import requests
import test_module
#from test_module import *
for method in dir():
    print(method)

print(test_module.math.sqrt(25))