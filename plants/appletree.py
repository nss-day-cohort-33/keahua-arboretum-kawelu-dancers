from .plant import Plant
from interfaces.habitat import IMountain
from interfaces.identifiable import Identifiable

class Apple_Tree(Plant, IMountain, Identifiable):

    def __init__(self):
        Plant.__init__(self, "Mountain Apple Tree")
        IMountain.__init__(self)
        Identifiable.__init__(self)




