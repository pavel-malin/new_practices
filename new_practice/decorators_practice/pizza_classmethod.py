class Pizza(object):
    def __init__(self, ingredints):
        self.ingredints = ingredints

    @classmethod
    def from_fridge(cls, fridge):
        return cls(fridge.get_cheese() + fridge.get_vegetables())
