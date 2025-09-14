from random import randint

class Cat:
    def __init__(self, name):
        self.name = name
        self.happiness = 50
        self.energy = 100
        self.saturation = 100
        self.alive = True
    def to_sleep(self):
        print("I`m tired, time to sleep")
        self.energy += 10
        self.happiness += 1
        self.saturation -= 6
    def to_play(self):
        print("I`m bored, time to play")
        self.energy -= 5
        self.happiness += 5
        self.saturation -= 8
    def to_eat(self):
        print("Saturation is low, time to eat")
        self.saturation += 15
        self.happiness += 3
        self.energy += 4
    def end_of_day(self):
        print(f"happiness = {self.happiness}")
        print(f"energy = {self.energy}")
        print(f"saturation = {self.saturation}")
    def life(self, day):
        text_day = f"Day{day} of {self.name} life"
        print(f"{text_day:=^40}")
        cube = randint(1, 3)
        if self.happiness <= 0:
            print("Died of boredom")
            self.alive = False
        elif self.energy <= 0:
            print("Died of energy deficiency")
            self.alive = False
        elif self.saturation <= 0:
            print("Became too hangry")
            self.alive = False
        if cube == 1:
            self.to_sleep()
        elif cube == 2:
            self.to_eat()
        elif cube == 3:
            self.to_play()
        self.end_of_day()
blaze = Cat(name = "Blaze")
for day in range(366):
    if blaze.alive == False:
        break
    blaze.life(day)