from .iaquatic import IAquatic

class IStagnant(IAquatic):
    def __init__(self):
        super().__init__()
        self.stagnant = True