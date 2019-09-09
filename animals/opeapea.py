from animals import Animal
from interfaces.habitat import IForest
from interfaces.habitat import IMountain
from interfaces import Identifiable

class Opeapea(Animal, IForest, IMountain, Identifiable):

    def __init__(self, age):
        Animal.__init__(self, "Ope'ape'a", age)
        IForest.__init__(self)
        IMountain.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Dragonfly", "Herbs", "Kale", "Centipede" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The ope\'ape\'a ate {prey} for a meal')
        else:
            print(f'The ope\'ape\'a rejects the {prey}')


    def __str__(self):
        return f'Opeapea {self.id}. SCREeeeeeechhhh!'