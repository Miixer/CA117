class Point(object):

    def __init__(self, x=0, y=0):
        self.x = int(x)
        self.y = int(y)

    def distance(self, other):
        x = self.x - other.x
        y = self.y - other.y
        d = (x ** 2 - y ** 2) ** 0.5

    def __str__(self):
        return 

