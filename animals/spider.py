from animals import Animal
from interfaces.habitat import IStagnant
from interfaces.identifiable import Identifiable

class Spider(Animal, IStagnant, Identifiable):

    def __init__(self, age):
        Animal.__init__(self, "Happy Face Spider", age)
        IStagnant.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Mosquitos", "Insects" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The spider ate {prey} for a meal')
        else:
            print(f'The spider rejects the {prey}')

    def __str__(self):
        return f'Spider {self.id}. WWWWEeeeeeeee!'