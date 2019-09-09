from interfaces import ITerrestrial
from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants


class Grassland(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
      IContainsAnimals.__init__(self)
      IContainsPlants.__init__(self)
      Identifiable.__init__(self)

    def add_animal(self, animal):
        try:
            if animal.terrestrial == True and animal.grassland_bound == True:
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add aquatic, or non-grassland animals to a grassland")

    def add_plant(self, plant):
        try:
            if plant.terrestrial == True and plant.grassland_bound == True:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError("Cannot add aquatic, or non-grassland plants to a grassland")