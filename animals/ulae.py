from animals import Animal
from interfaces.habitat import ISaltwater
from interfaces.identifiable import Identifiable

class Ulae(Animal, ISaltwater, Identifiable):

    def __init__(self, age):
        Animal.__init__(self, "Ulae", age)
        ISaltwater.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "snail", "lizard", "guppie" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The ulae ate a {prey} for a meal!')
        else:
            print(f'The ulae rejects the {prey}.')


    def __str__(self):
        return f'Ulae {self.id}. RRRRoarrrrrr!'