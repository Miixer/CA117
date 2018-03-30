class Employee(object):

   next_employee_number = 0

   def __init__(self, name, hourly_rate=9.25, hours_worked=0):
      self.name = name
      self.ID = Employee.next_employee_number
      self.rate = hourly_rate
      self.hours = hours_worked
      Employee.next_employee_number += 1

   def add_hours(self, other):
      z = self.hours + other
      self.hours = z
      return self

   def __str__(self):
      name = "Name: {}".format(self.name)
      iD = "ID: {}".format(self.ID)
      hours = "Hours: {:.2f}".format(self.hours)
      rate = "Rate: {:.2f}".format(self.rate)
      wages = "Wages: {:.2f}".format(self.hours*self.rate)
      return "\n".join([name, iD, hours, rate, wages])

def main():

    # Check class attributes
    print('Checking class attributes...')
    print(Employee.next_employee_number)
    
    # Create two employees
    e1 = Employee('Jimmy')
    e2 = Employee('Mary', hours_worked=12, hourly_rate=12.40)

    # Check string representation
    print('Printing employees...')
    print(e1)
    print(e2)

    # Check adding hours
    print('Checking adding hours...')
    e1.add_hours(10.5)
    e2.add_hours(30)
    print(e1)
    print(e2)

    # Check class attributes
    print('Checking class attributes...')    
    print(Employee.next_employee_number)

if __name__ == '__main__':
    main()