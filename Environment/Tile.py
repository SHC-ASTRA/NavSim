from enum import Enum


class Terrain_Type(Enum):
    OBSTACLE = 0
    CLEAR = 1


class Tile:
    def __init__(self, terr_type):
        # If input is not a terrain type, throw error
        if type(terr_type) != Terrain_Type:
            raise TypeError(
                "Must be intialized with a proper terrain type.\
                \nSee /Environment/Tile.py"
            )
        self.terr_type = terr_type