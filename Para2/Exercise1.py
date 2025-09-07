class Student:
    def __init__(self, height = 170):
        self.height = height

vasiliy = Student()
petro = Student(height = 180)

print(vasiliy.height)
print(petro.height)
