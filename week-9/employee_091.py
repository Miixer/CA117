class Employee(object):

   def __init__(self, name, ID):
      self.name = name
      self.ID = ID

   def wages(self):
      wage = 0
      return wage

   def __str__(self):
      name = "Name: {}".format(self.name)
      num = "Number: {}".format(self.ID)
      wages = "Wages: {:.2f}".format(self.wages())
      return "\n".join([name, num, wages])

class Manager(Employee):
   def __init__(self, name, ID, salary):
      super().__init__(name, ID)
      self.salary = salary

   def wages(self):
      return self.salary / 52

class AssemblyWorker(Employee):
   def __init__(self, name, ID, hourly_rate, hours):
      super().__init__(name, ID)
      self.rate = hourly_rate
      self.hours = hours

   def wages(self):
      return self.rate * self.hours
      
def main():

    e1 = Manager('Mary', 1, 50000)
    e2 = AssemblyWorker('Fred', 2, 15.50, 40)
    e3 = Employee('Sean', 3)

    print(e1)
    print(e2)
    print(e3)

if __name__ == '__main__':
   main()
