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

    def add_animal(self, animal):
        try:
            if animal.aquatic == True and animal.fresh == True:
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add non-aquatic, or saltwater animals to a river")

    def add_plant(self, plant):
        try:
            if plant.aquatic == True and plant.fresh == True:
                self.plants.append(plant)
        except AttributeError:
            raise AttributeError("Cannot add plants that require brackish water or stagnant water to a river")
