from abc import ABCMeta, abstractmethod
from copy import deepcopy


class Prototype(metaclass=ABCMeta):
    @abstractmethod
    def clone(self):
        pass
    

class Car(Prototype):
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
        
    def clone(self):
        return deepcopy(self)
        
        
car_1 = Car('Dodge', 'Challenger SRT', 2021)
cloned_car = car_1.clone()

print(car_1)
print(cloned_car)
print(car_1 == cloned_car)