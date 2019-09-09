from interfaces import IAquatic
from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants


class Swamp(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
      IContainsAnimals.__init__(self)
      IContainsPlants.__init__(self)
      Identifiable.__init__(self)

    def add_animal(self, animal):
        try:
            if animal.aquatic == True and animal.stagnant == True:
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add non-aquatic, or saltwater animals to a swamp")

    def add_plant(self, plant):
        try:
            if plant.aquatic == True and plant.stagnant == True:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError("Can only add plants that require stagnant water to a swamp")
