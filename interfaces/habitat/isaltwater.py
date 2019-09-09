from .iaquatic import IAquatic

class ISaltwater(IAquatic):

    def __init__(self):
        super().__init__()
        self.salty = True
