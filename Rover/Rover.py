

class Rover:
    def __init__(self, mass=10, rotation=0, position=None,
                 ):
        if position is None:
            position = [0, 0]

        if type(mass) != float and type(mass) != int:
            raise TypeError(
                "Mass parameter must be an integer or floating point value."
            )
        self.mass = float(mass)
        
        if type(rotation) != float and type(rotation) != int:
            raise TypeError(
                "Rotation parameter must be an integer or floating point value."
            )
        self.rotation = float(rotation)

        if (type(position) != list and type(position) != tuple) or len(position) != 2:
            raise TypeError(
                "Position parameter must be a list or tuple of with len=2."
            )
        elif all(type(x) == int or type(x) == float for x in position):
            raise TypeError(
                "Position array must comprise of integers and/or floats."
            )

        self.position = list(position)
