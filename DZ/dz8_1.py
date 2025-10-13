pass

'''Task 1'''

class IterableGenerator:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        # Повертаємо генератор
        def generator():
            for i in range(1, self.n + 1):
                yield i * i  # наприклад, квадрати чисел

        return generator()

print('=======================')
print('=======================')
print('=======================')
print('=======================')
print('=======================')

'''Task 2'''
for value in IterableGenerator(5):
    print(value)


def safe_calculator(func):
    def wrapper(expression):
        try:
            if not isinstance(expression, str):
                raise ValueError("Expression must be a string")
            result = func(expression)
            print(f"Result of '{expression}' is {result}")
            return result
        except ZeroDivisionError:
            print("Error: Division by zero!")
        except Exception as e:
            print(f"Error: {e}")

    return wrapper

@safe_calculator
def calculate(expression):
    import ast, operator
    allowed_ops = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.Mod: operator.mod,
        ast.USub: operator.neg
    }

    def eval_node(node):
        if isinstance(node, ast.Constant):
            return value
        elif isinstance(node, ast.BinOp):
            left = eval_node(node.left)
            right = eval_node(node.right)
            op_type = type(node.op)
            if op_type in allowed_ops:
                return allowed_ops[op_type](left, right)
            else:
                raise ValueError(f"Operator {op_type} not allowed")
        elif isinstance(node, ast.UnaryOp):
            operand = eval_node(node.operand)
            op_type = type(node.op)
            if op_type in allowed_ops:
                return allowed_ops[op_type](operand)
            else:
                raise ValueError(f"Operator {op_type} not allowed")
        else:
            raise TypeError(node)

    node = ast.parse(expression, mode='eval').body
    return eval_node(node)

calculate("2 + 3 * 5")
calculate("10 / 0")
calculate("2 + unknown_var")

print('=======================')
print('=======================')
print('=======================')
print('=======================')
print('=======================')


'''Task 3'''

from random import randint


class Student:
    def __init__(self, name):
        self.name = name
        self.happiness = 50
        self.progress = 0
        self.alive = True
        self.day = 0  # поточний день

    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.happiness -= 3

    def pull_an_allnighter(self):
        print("Exam coming, time to study hard!")
        self.progress += 0.5
        self.happiness -= 10

    def to_sleep(self):
        print("Time to sleep")
        self.happiness += 3

    def to_chill(self):
        print("Rest time")
        self.happiness += 5
        self.progress -= 0.1

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out ;(")
            self.alive = False
        elif self.happiness <= 0:
            print("Depression")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally!")
            self.alive = False

    def end_of_day(self):
        print(f"happiness = {self.happiness}")
        print(f"progress = {round(self.progress, 2)}")

    def life(self):
        text_day = f"Day {self.day} of {self.name} life"
        print(f"{text_day:=^30}")
        cube = randint(1, 4)
        if cube == 1:
            self.to_sleep()
        elif cube == 2:
            self.to_study()
        elif cube == 3:
            self.to_chill()
        else:
            self.pull_an_allnighter()
        self.end_of_day()
        self.is_alive()
        self.day += 1

    def __iter__(self):
        while self.alive:
            yield self.life()

nickolas = Student("Nick")
for _ in nickolas:
    pass
