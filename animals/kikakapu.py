from animals import Animal
from interfaces.habitat import IFreshwater
from interfaces.habitat import IStagnant
from interfaces.identifiable import Identifiable

class Kikakapu(Animal, IFreshwater, IStagnant, Identifiable):

    def __init__(self, age):
        Animal.__init__(self, "Kikakapu", age)
        IFreshwater.__init__(self)
        IStagnant.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Algae", "Coral Polyps", "Worms", "Shrimp"}

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The kikakapu ate {prey} for a meal')
        else:
            print(f'The kikakapu rejects the {prey}')

    def __str__(self):
        return f'Kikakapu {self.id}.!'