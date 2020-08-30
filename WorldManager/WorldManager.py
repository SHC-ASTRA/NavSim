from Environment.Tilemap import *
from Rover.Rover import *


class World_Manager:
    def __init__(self, rover, tilemap):
        if type(rover) != Rover:
            raise TypeError(
                "Must be initialized with a Rover class.\
                \nSee /Rover/Rover.py"
            )
        self.rover = rover

        if type(tilemap) != Tilemap:
            raise TypeError(
                "Must be initialized with a Tilemap class.\
                \nSee /Environment/Tilemap.py"
            )
        self.tilemap = tilemap
