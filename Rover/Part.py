class Part:
    def __init__(self, rel_x, rel_y):
        accepted_types = [int, float]
        if type(rel_x) not in accepted_types or type(rel_y) not in accepted_types:
            raise TypeError(
                "Part must be initialized with relative x and y position of type int or float."
            )
        self.rel_x = float(rel_x)
        self.rel_y = float(rel_y)

    def get_rel_x(self):
        return self.rel_x

    def get_rel_y(self):
        return self.rel_y
