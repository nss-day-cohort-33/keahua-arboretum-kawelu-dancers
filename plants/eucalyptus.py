from plant import Plant
from interfaces.habitat import IForest
from interfaces import Identifiable

class Eucalyptus(Plant, IForest, Identifiable):

    def __init__(self):
        Plant.__init__(self, "Rainbow Eucalyptus Tree")
        IForest.__init__(self)
        Identifiable.__init__(self)