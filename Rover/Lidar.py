from .Part import Part

# This is temporary, should be rewritten once we have actual things to put here
# This template can be used to define any simple extension of Part
class Lidar(Part):
    def __init__(self, *args):
        super().__init__(args[0], args[1])
