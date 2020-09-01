class Part:
    def __init__(self, rel_x, rel_y):
        if type(rel_x) != float or type(rel_y) != float:
            raise TypeError(
                "Part must be initialized with relative x and y position of type float."
            )
        self.rel_x = rel_x
        self.rel_y = rel_y
