import random

# ---------- Базові класи ----------
class Engine:
    def __init__(self, power):
        self.power = power  # унікальний атрибут
    def start_engine(self):
        return f"Engine started with {self.power} HP."


class Wheels:
    def __init__(self, wheel_count):
        self.wheel_count = wheel_count  # унікальний атрибут
    def rotate(self):
        return f"All {self.wheel_count} wheels are spinning."


class Body:
    def __init__(self, color):
        self.color = color  # унікальний атрибут
    def paint(self, new_color):
        self.color = new_color
        return f"The body has been painted {self.color}."


# ---------- Клас, породжений кількома ----------
class Car(Engine, Wheels, Body):
    def __init__(self, power, wheel_count, color, brand):
        Engine.__init__(self, power)
        Wheels.__init__(self, wheel_count)
        Body.__init__(self, color)
        self.brand = brand  # власний атрибут
    def drive(self):
        start = self.start_engine()
        spin = self.rotate()
        return f"{self.brand} is driving! {start} {spin}"


# ---------- Перевірка ----------
car1 = Car(300, 4, "red", "Ferrari")
print(car1.drive())
print(car1.paint("black"))
print(car1.start_engine())
print(car1.rotate())
