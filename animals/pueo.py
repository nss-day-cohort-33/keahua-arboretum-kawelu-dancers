from animals import Animal
from interfaces.habitat import IGrassland
from interfaces.habitat import IForest
from interfaces.identifiable import Identifiable

class Pueo(Animal, IGrassland, IForest, Identifiable):

    def __init__(self, age):
        Animal.__init__(self, "Pueo", age)
        IForest.__init__(self)
        IGrassland.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Mice", "Hedgehog", "Possum", "Rodent" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The pueo ate {prey} for a meal')
        else:
            print(f'The pueo rejects the {prey}')


    def __str__(self):
        return f'Pueo {self.id}. Hoot Hoot!'