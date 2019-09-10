from interfaces.habitat import IAquatic
from interfaces.identifiable import Identifiable
from interfaces.habitat import IContainsAnimals
from interfaces.habitat import IContainsPlants


class Swamp(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
      IContainsAnimals.__init__(self)
      IContainsPlants.__init__(self)
      Identifiable.__init__(self)
      self.type = "swamps"
      self.max_animals = 8
      self.max_plants = 12

