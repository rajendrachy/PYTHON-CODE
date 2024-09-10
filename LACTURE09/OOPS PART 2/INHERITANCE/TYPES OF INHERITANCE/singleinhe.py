# eg of the single inheritance

class Car:
    @staticmethod
    def start():
        print("Car start")

    @staticmethod
    def stop():
        print("Car stop")


class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")


print(car1.name)
print(car1.start())
print(car2.name)

