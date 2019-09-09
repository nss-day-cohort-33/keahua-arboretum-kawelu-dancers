from interfaces import IAquatic
from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants


class Coastline(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
      IContainsAnimals.__init__(self)
      IContainsPlants.__init__(self)
      Identifiable.__init__(self)

    def add_animal(self, animal):
        try:
            if animal.aquatic == True and animal.salty == True:
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add terrestrial, or non-coastline animals to a coastline")

    def add_plant(self, plant):
        try:
            if plant.aquatic == True and plant.salty == True:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError("Cannot add terrestrial, or non-coastline plants to a coastline")