from .terrestrial import ITerrestrial

class IMountain(ITerrestrial):
    def __init__(self):
        super().__init__()
        self.mountain_bound = True