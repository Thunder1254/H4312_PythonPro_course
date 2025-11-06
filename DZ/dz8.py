import random
import logging

# ---------- Logging setup ----------
logging.basicConfig(
    filename="simulation.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ---------- Data ----------
brands_of_car = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 70, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14}
}

job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 45, "gladness_less": 25},
    "Rust developer": {"salary": 70, "gladness_less": 1}
}


# ---------- Classes ----------
class Human:
    def __init__(self, name="Human", job=None, car=None, home=None):
        self.name = name
        self.job = job
        self.car = car
        self.home = home
        self.money = 100
        self.gladness = 50
        self.satiety = 50

    def get_home(self):
        self.home = House()
        logging.info(f"{self.name} settled in a new house")

    def get_car(self):
        self.car = Auto(brands_of_car)
        logging.info(f"{self.name} bought a car {self.car.brand}")

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
        self.job = Job(job_list)
        logging.info(f"{self.name} got a job as {self.job.job}")

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety >= 100:
                self.satiety = 100
                return
            self.satiety += 5
            self.home.food -= 5
        logging.info(f"{self.name} ate, satiety = {self.satiety}")

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4
        logging.info(f"{self.name} worked, money = {self.money}")

    def shopping(self, manage):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            logging.info(f"{self.name} bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manage == "food":
            logging.info(f"{self.name} bought food")
            self.money -= 50
            self.home.food += 50
        elif manage == "delicacies":
            logging.info(f"{self.name} bought delicacies")
            self.gladness += 10
            self.satiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 10
        self.home.mess += 5
        logging.info(f"{self.name} is chilling, gladness = {self.gladness}")

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0
        logging.info(f"{self.name} cleaned home")

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50
        logging.info(f"{self.name} repaired the car")

    def is_alive(self):
        if self.gladness < 0:
            logging.warning(f"{self.name} is in depression")
            return False
        if self.satiety < 0:
            logging.warning(f"{self.name} died of hunger")
            return False
        if self.money < -500:
            logging.warning(f"{self.name} went bankrupt")
            return False
        return True

    def live(self, day):
        if not self.is_alive():
            return False
        if self.home is None:
            self.get_home()
        if self.car is None:
            self.get_car()
        if self.job is None:
            self.get_job()

        dice = random.randint(1, 4)
        if self.satiety < 20:
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 15:
                self.clean_home()
            else:
                self.chill()
        elif self.money < 0:
            self.work()
        elif self.car.strength < 15:
            self.to_repair()
        elif dice == 1:
            self.chill()
        elif dice == 2:
            self.work()
        elif dice == 3:
            self.clean_home()
        elif dice == 4:
            self.shopping("delicacies")
        return True


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list.keys()))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.strength -= 1
            self.fuel -= self.consumption
            return True
        else:
            logging.warning(f"The {self.brand} car cannot move")
            return False


class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list.keys()))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job_list[self.job]["gladness_less"]


# ---------- Run Simulation ----------
persona1 = Human("Vasiliy")
for day in range(1, 366):
    if not persona1.live(day):
        break
