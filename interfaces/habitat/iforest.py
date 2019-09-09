from .terrestrial import ITerrestrial

class IForest(ITerrestrial):
    def __init__(self):
        super().__init__()
        self.forest_bound = True