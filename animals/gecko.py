from animals import Animal
from interfaces.habitat import IForest
from interfaces.identifiable import Identifiable

class Gecko(Animal, IForest, Identifiable):

    def __init__(self, age):
        Animal.__init__(self, "Gold Dust Day Gecko", age)
        IForest.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Crickets", "Baby food", "Flies"}

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Gold Dust Day Gecko ate {prey} for a meal')
        else:
            print(f'The Gold Dust Day Gecko rejects the {prey}')

    def __str__(self):
        return f'Gold Dust Day Gecko {self.id}. tititititick!'