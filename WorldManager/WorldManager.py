from Environment.Tilemap import *
from Rover.Rover import *
from WorldManager.DummyPhysics import *


class WorldManager:
    def __init__(self, rover, time_scale=1.0):
        """Initializes a WorldManager instance.

        Keyword Arguments:
        rover -- an instance of the Rover class
        timescale -- how fast should the simulation run relative to real life
        """
        if type(rover) != Rover:
            raise TypeError(
                "rover parameter must be a Rover class.\
                \nSee /Rover/Rover.py"
            )
        self.rover = rover

        if type(time_scale) not in [int, float]:
            raise TypeError(
                "timescale parameter must be an integer or floating point number."
            )
        self.timescale = time_scale
        self.time_elapsed = 0

        self.tilemap = Tilemap()

    def update(self, timestep):
        simtimestep = timestep * self.timescale

        update_physics(self.rover, self.tilemap, simtimestep)

        self.time_elapsed += simtimestep

