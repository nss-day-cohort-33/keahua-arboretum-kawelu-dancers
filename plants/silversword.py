from plant import Plant
from interfaces.habitat import IGrassland
from interfaces import Identifiable

class Silversword(Plant, IGrassland, Identifiable):

    def __init__(self):
        Plant.__init__(self, "Silversword")
        IGrassland.__init__(self)
        Identifiable.__init__(self)