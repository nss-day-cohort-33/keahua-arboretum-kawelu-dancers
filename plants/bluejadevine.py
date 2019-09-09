from plant import Plant
from interfaces.habitat import IGrassland
from interfaces.habitat import IStagnant
from interfaces.identifiable import Identifiable

class Blue_Jade_Vine(Plant, IGrassland, IStagnant, Identifiable):

    def __init__(self):
        Plant.__init__(self, "Blue Jade Vine")
        IGrassland.__init__(self)
        IStagnant.__init__(self)
        Identifiable.__init__(self)