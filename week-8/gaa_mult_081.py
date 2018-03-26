class Score(object):

   def __init__(self, goals=0, points=0):
      self.goals = goals
      self.points = points
      self.total = (self.goals*3) + self.points

   def __eq__(self, other):
      return self.total == other.total

   def __gt__(self, other):
      return self.total > other.total

   def __ge__(self, other):
      return self.total >= other.total

   def __lt__(self, other):
      return self.total < other.total

   def __le__(self, other):
      return self.total <= other.total

   def __add__(self, other):
      g = self.goals + other.goals
      p = self.points + other.points
      return Score(g, p)

   def __sub__(self, other):
      g = self.goals - other.goals
      p = self.points - other.points
      return Score(g, p)

   def __iadd__(self, other):
      g = self.goals + other.goals
      p = self.points + other.points

      self.goals, self.points = g, p
      return self

   def __isub__(self, other):
      g = self.goals - other.goals
      p = self.points - other.points

      self.goals, self.points = g, p
      return self

   def __mul__(self, other):
      g = self.goals * other
      p = self.points * other
      return Score(g, p)

   def __rmul__(self, other):
      g = self.goals * other
      p = self.points * other
      return Score(g, p)

   def __imul__(self, other):
      g = self.goals * other
      p = self.points * other
      
      self.goals, self.points = g, p
      return self

   def __str__(self):
      return "{} goal(s) and {} point(s)".format(self.goals, self.points)

def main():

   # Create some instances of Score
   s1 = Score()
   s2 = Score(3, 12)
   s3 = Score(4, 9)
   s4 = Score(2, 11)
   s5 = Score(1, 1)

   # Display
   print('Display...')
   print(s1)
   print(s2)
   print(s3)
   print(s4)

   # Multiplication
   print('Multiplication...')
   s2 = s2 * 2
   print(s2)
   print(s2 > s3)

   # Right multiplication
   print('Right multiplication...')
   s2 = 2 * s2
   print(s2)
   print(s2 > s3)

   # In-place multiplication
   print('In-place multiplication...')
   s2alias = s2
   s2 *= 2
   print(s2)
   print(s2alias)
   print(s2 == s2alias)

if __name__ == '__main__':
   main()