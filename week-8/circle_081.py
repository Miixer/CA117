class Point(object):
   def __init__(self, x=0, y=0):
      self.x = x
      self.y = y
   def midpoint(self, other):
      xd = (self.x + other.x) / 2
      yd = (self.y + other.y) / 2
      return xd, yd
   def __str__(self):
      return "Point: ({}, {})".format(self.x, self.y)

class Circle(object):
   def __init__(self, p = Point(0,0), radius=0):
      self.radius = int(radius)
      self.point = p
   def __add__(self, other):
      nx, ny = Point.midpoint(self.point, other.point)
      nradius = self.radius + other.radius
      return Circle(Point(nx,ny), nradius)
   def __str__(self):
      return "Centre: ({:.1f}, {:.1f})\nRadius: {}".format(self.point.x, self.point.y, self.radius)


def main():
   p1 = Point()
   p2 = Point(4,6)
   c1 = Circle(p1, 10)
   c2 = Circle(p2, 5)
   c3 = c1 + c2
   print(c3)

   p3 = Point(10,10)
   c4 = Circle(p3,15)
   c5 = c2 + c4
   print(c5)
    
if __name__ == '__main__':
    main()