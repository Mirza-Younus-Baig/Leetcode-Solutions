
class Car:
    def __init__(self, make, wheels = 4, engine = "Oil", mileage = 20000) -> None:
        self.wheels = wheels
        self.engine = engine
        self.make = make
        self.mileage = mileage
    def carMake(self):
        return self.make
    
    def updateMileage(self, func, update):
        return map(func, )

myCar = Car("Tesla")
print(myCar.carMake())
