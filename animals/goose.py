from animals import Animal
from interfaces.habitat import IGrassland
from interfaces import Identifiable

class Goose(Animal, IGrassland, Identifiable):

    def __init__(self, age):
        Animal.__init__(self, "NeNe Goose", age)
        IGrassland.__init__(self)
        Identifiable.__init__(self)
        self.__prey = { "Fruit", "Seeds", "Flowers", "Shrubbery" }

    @property
    def prey(self):
        return self.__prey

    def feed(self, prey):
        if prey in self.__prey:
            print(f'The Nene goose ate {prey} for a meal')
        else:
            print(f'The Nene goose rejects the {prey}')


    def __str__(self):
        return f'Nene Goose {self.id}. Honk Honk Honk!'