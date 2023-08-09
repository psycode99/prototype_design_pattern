from abc import ABCMeta, abstractmethod
from copy import deepcopy

class Prototype(metaclass=ABCMeta):
    @abstractmethod
    def clone(self):
        pass

class Knight(Prototype):
    def __init__(self, level) -> None:
        self.unit_type = 'knight'
        filename = "{}_{}.dat".format(self.unit_type, level)
        with open(filename, 'r') as params_file:
            line = params_file.readlines()
        
            self.life = line[0]
            self.speed = line[1]
            self.attack_power = line[2]
            self.attack_range = line[3]
            self.weapon = line[4]
            
    
    def clone(self):
        return deepcopy(self)
            
            

class Archer(Prototype):
     def __init__(self, level) -> None:
        self.unit_type = 'archer'
        filename = "{}_{}.dat".format(self.unit_type, level)
        with open(filename, 'r') as params_file:
            line = params_file.readlines()
        
            self.life = line[0]
            self.speed = line[1]
            self.attack_power = line[2]
            self.attack_range = line[3]
            self.weapon = line[4]
            
    
     def clone(self):
        return deepcopy(self)
  
  
class Barracks():
    def __init__(self):
      self.units = {
          'knight':{
              1: Knight(1),
            #   2: Knight(2)
          },
          'archer':{
              1: Archer(1),
            #   2: Archer(2)
          }
      }
  
    def generate_unit(self, unit_type, level):
        return self.units[unit_type][level]
        
        
barracks = Barracks()
knight_1 = barracks.generate_unit('knight', 1)
archer_1 = barracks.generate_unit('archer', 1)
archer_1.weapon = "poisoned arrow"

archer_2 = archer_1.clone()
print(archer_1)
print(archer_2)

print(archer_2.weapon)
print(knight_1.weapon)
print(archer_1.weapon)