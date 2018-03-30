class Time(object):

   def __init__(self, hour=0, minute=0, second=0):
      self.hour = hour
      self.min = minute
      self.sec = second

   def __eq__(self, other):
      return ((self.hour, self.min, self.sec) == (other.hour, other.min, other.sec))

   def __gt__(self, other):
      return self.time_to_seconds() > other.time_to_seconds()

   def __add__(self, other):
      return self.seconds_to_time(self.time_to_seconds() + other.time_to_seconds())

   def __iadd__(self, other):
      z = self + other
      self.hour, self.min, self.sec = z.hour, z.min, z.sec
      return self

   def __str__(self):
      return ("The time is {:02d}:{:02d}:{:02d}".format(self.hour, self.min, self.sec))

   def time_to_seconds(self):
      return self.hour*60*60 + self.min*60 + self.sec

   @classmethod
   def seconds_to_time(cls, s):
      m, s = divmod(s, 60)
      h, m = divmod(m, 60)
      of, h = divmod(h, 24)
      return cls(h,m,s)

def main():

    t1 = Time()
    t2 = Time(9,35,16)
    t3 = Time(0,0,4)
    t4 = Time(9,35,16)

    # Check string representation
    print('Printing times...')
    print(t1)
    print(t2)
    print(t3)

    # Check equality
    print('Checking equality...')
    print(t2 == t4)
    print(t1 == t3)

    # Check greater than/less than
    print('Checking greater than/less than...')
    print(t2 > t3)
    print(t2 < t3)
    print(t4 > t1)
    print(t4 < t1)

    # Check addition
    print('Checking addition...')
    t5 = t2 + t2 + t2
    print(t5)
    print(t5 > t2)

    # Check increment
    print('Checking increment...')
    t33 = t2
    t2 += t2
    t2 += t4
    print(t2)
    print(t33 is t2)
    print(t2 > t3)

    # Check class method
    print('Checking class method...')
    t6 = Time.seconds_to_time(123456)
    print(t6)
    print(t6 > t1)

if __name__ == '__main__':
   main()