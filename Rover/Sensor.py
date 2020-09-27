from Rover.Part import Part


class Sensor(Part):
    def __init__(self, *args):
        super().__init__(*args)

    def update(self, rover, tilemap, timestep):
        raise NotImplementedError("Please implement an update function for this sensor.")
