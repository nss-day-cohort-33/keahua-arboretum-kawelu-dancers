from interfaces.habitat import IAquatic
from interfaces.identifiable import Identifiable
from interfaces.habitat import IContainsAnimals
from interfaces.habitat import IContainsPlants
from animals import RiverDolphin

class River(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
      IContainsAnimals.__init__(self)
      IContainsPlants.__init__(self)
      Identifiable.__init__(self)
      self.type = "rivers"
      self.max_animals = 12
      self.max_plants = 6
