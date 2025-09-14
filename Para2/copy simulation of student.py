from random import randint

class Student:
    def __init__(self, name, targets_in_life):
        self.name = name
        self.happiness = 50
        self.progress = 0
        self.money = 0
        self.alive = True
        self.targets_in_life = targets_in_life
    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.happiness -= 3
        self.money -= 3
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
        self.money -= 1
    def work(self):
        print("Time to work")
        self.money += 5
        self.progress += 0.1
        self.happiness -= 4
    def is_alive(self):
        pass
    def end_of_day(self):
        print(f"happiness = {self.happiness}")
        print(f"progress = {round(self.progress, 2)}")
        print(f"money = {self.money}")
    def targets(self, day):
        text_day = f"Day{day} of {self.name} life"
        print(f"{text_day:=^30}")
        print(f"{self.targets_in_life}")
        cube = randint(1, 5)
        goalscube = randint(1, 3)
        if self.targets_in_life == "school":
            if self.progress < -0.5:
                print("Cast out ;(")
                print("Change of goals to Money")
                self.targets_in_life = "Money"
            elif self.happiness <= 0:
                print("Depression")
                print("Change of goals to Happiness")
                self.targets_in_life = "Happiness"
                self.alive = False
            elif self.progress > 5:
                print("Passed externally!")
                print("Time to chase success/money")
                self.targets_in_life = "Money"
                self.alive = False
            elif self.money <= 0:
                print("Im poor :(")
                self.work()
                print("The university forced me to work.")
            if cube == 1:
                 self.to_sleep()
            elif cube == 2:
                    self.to_study()
            elif cube == 3:
                    self.to_chill()
            elif cube == 4:
                self.pull_an_allnighter()
            else:
                self.work()
        elif self.targets_in_life == "Money":
            if goalscube == 1:
                self.work()
            elif goalscube == 2:
                self.to_sleep()
            elif goalscube == 3:
                self.to_chill()
        elif self.targets_in_life == "Happiness":
            if goalscube == 1:
                self.to_chill()
            elif goalscube == 2:
                self.to_sleep()
            elif goalscube == 3:
                self.work()
        self.end_of_day()
        self.is_alive()
nickolas = Student(name= "Nick", targets_in_life = "school")
for day in range(366):
    nickolas.targets(day)


