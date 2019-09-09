from interfaces.habitat import ITerrestrial
from interfaces.identifiable import Identifiable
from interfaces.habitat import IContainsAnimals
from interfaces.habitat import IContainsPlants


class Mountain(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
      IContainsAnimals.__init__(self)
      IContainsPlants.__init__(self)
      Identifiable.__init__(self)

    def add_animal(self, animal):
        try:
            if animal.terrestrial == True and animal.mountain_bound == True:
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add aquatic, or non-mountain animals to a mountain")

    def add_plant(self, plant):
        try:
            if plant.terrestrial == True and plant.mountain_bound == True:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError("Cannot add aquatic, or non-mountain plants to a mountain")