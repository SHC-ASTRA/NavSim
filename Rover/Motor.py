from .Part import Part


class Motor(Part):
    # Default speed of zero
    def __init__(self, rel_x, rel_y, speed=0.0):
        if type(speed) != float:
            # Save error for end of init
            e = TypeError(
                "Motor cannot be initialized with a speed that is not of type float."
            )
        self.speed = speed
        super().__init__(rel_x, rel_y)
        # Raise here such that errors in passed args will hit the Part constructor first
        raise e
