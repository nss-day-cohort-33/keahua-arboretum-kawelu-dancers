from .iaquatic import IAquatic

class IFreshwater(IAquatic):

    def __init__(self):
        super().__init__()
        self.fresh = True
