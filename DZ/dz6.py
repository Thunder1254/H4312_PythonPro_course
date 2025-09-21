import colorama as clrm
import inspect
import sys
print(inspect.ismodule(clrm))
print(inspect.isclass(clrm))
print(inspect.isfunction(clrm))
help(clrm)
clrma = clrm
print(clrm.__name__)
print(clrma.__name__)

for module_name, module_path in sys.modules.items():
    print(module_name, module_path)
    print("----------------------")
for variable in dir(__builtins__):
    print(variable)