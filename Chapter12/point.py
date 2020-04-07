class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def coor(self):
        """coor

        :return: tuple of coordinate
        """
        return (self.x, self.y)

    def move(self, x, y):
        self.x = self.x + x
        self.y = self.y + y


point = Point(1, 1)
print(point.coor())
