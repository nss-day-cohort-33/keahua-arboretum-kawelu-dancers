from .iterrestrial import ITerrestrial

class IGrassland(ITerrestrial):
    def __init__(self):
        super().__init__()
        self.grassland_bound = True