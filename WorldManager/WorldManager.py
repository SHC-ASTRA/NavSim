from Environment.Tilemap import *
from Rover.Rover import *


class WorldManager:
    def __init__(self, rover, tilemap):
        """Initializes a WorldManager instance.

        Keyword Arguments:
        rover -- an instance of the Rover class
        tilemap -- an instance of a TileMap class
        """
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
