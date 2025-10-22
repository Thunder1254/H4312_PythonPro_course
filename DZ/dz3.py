import random

class Cow:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.milk = 0

    def eat_grass(self):
        self.hunger += 10
        print(f"{self.name} is eating grass. Hunger: {self.hunger}")

    def produce_milk(self):
        if self.hunger > 20:
            self.milk += 5
            self.hunger -= 5
            print(f"{self.name} produced milk! Milk amount: {self.milk}")
        else:
            print(f"{self.name} is too hungry to produce milk.")

class Farmer:
    def __init__(self, name, cow):
        self.name = name
        self.cow = cow
        self.milk_storage = 0

    def feed_cow(self):
        print(f"{self.name} feeds {self.cow.name}")
        self.cow.eat_grass()

    def milk_cow(self):
        if self.cow.milk >= 5:
            self.milk_storage += self.cow.milk
            print(f"{self.name} milks {self.cow.name}. Total milk stored: {self.milk_storage}")
            self.cow.milk = 0
        else:
            print(f"{self.cow.name} has not produced enough milk yet.")

    def live_day(self, day):
        print(f"\nDay {day} on the farm:")
        dice = random.randint(1, 3)
        if dice == 1:
            self.feed_cow()
        elif dice == 2:
            self.cow.produce_milk()
        elif dice == 3:
            self.milk_cow()


bessie = Cow("Bessie")
farmer = Farmer("John", bessie)

for day in range(1, 6):
    farmer.live_day(day)
