class Point(object):

   def __init__(self, x=0, y=0):
      self.x = int(x)
      self.y = int(y)

   def distance(self, object):
      x = self.x - object.x
      y = self.y - object.y
      d = (x ** 2 + y ** 2) ** 0.5
      return d

   def __str__(self):
      return "({:.1f}, {:.1f})".format(self.x, self.y)

class Segment(object):

   def __init__(self, p1, p2):
      self.p1 = p1
      self.p2 = p2

   def midpoint(self):
      low = self.p1
      high = self.p2
      xdist = (low.x + high.x) / 2
      ydist = (low.y + high.y) / 2
      return "({:.1f}, {:.1f})".format(xdist, ydist)

   def length(self):
      return ((self.p1).distance(self.p2))

class Circle(object):

   def __init__(self, point, radius):
      self.rad = int(radius)
      self.cen = point

   def overlaps(self, object):
      totalrad = self.rad + object.rad
      d = ((self.cen).distance(object.cen))
      return (totalrad > d)

def main():
   p1 = Point()
   p2 = Point(5, 5)
   s1 = Segment(p1, p2)
   s2 = Segment(p2, p1)
   c1 = Circle(p1, 5)
   c2 = Circle(p2, 2)
   c3 = Circle(p1, 2)

   print(p1)
   print(p2)
   print(s1.midpoint())
   print(s2.midpoint())
   print(c1.overlaps(c2))
   print(c2.overlaps(c1))
   print(c1.overlaps(c3))
   print(c3.overlaps(c2))

if __name__ == '__main__':
    main()