class Car:
    def __init__(self, type):  # typo: __inti__ -> __init__
        self.type = type  # assign type to an instance variable

    @staticmethod
    def start():
        print("car start")

    @staticmethod
    def stop():
        print("car stopped")


class ToyotaCar(Car):
    def __init__(self, name, type):
        super().__init__(type)  # call the parent's __init__ method
        self.name = name
        Car.start()  # call the static method on the parent class


car1 = ToyotaCar("prius", "electric")        
print(car1.type)  # prints: electric