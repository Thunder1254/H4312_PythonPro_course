from random import randint

class Student:
    def __init__(self, name):
        self.name = name
        self.happiness = 50
        self.progress = 0
        self.alive = True
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
    def life(self, day):
        text_day = f"Day{day} of {self.name} life"
        print(f"{text_day:=^30}")
        cube = randint(1,4)
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
nickolas = Student(name= "Nick")
for day in range(365):
    if nickolas.alive == False:
        break
    nickolas.life(day)
