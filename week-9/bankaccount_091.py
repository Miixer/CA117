class BankAccount(object):
  next_account_number = 16555232
  account_type = "General"

  def __init__(self, forename, surname, balance):
    self.name = forename
    self.sur = surname
    self.bal = balance
    self.iban = BankAccount.next_account_number
    BankAccount.next_account_number += 1

  def lodge(self, other):
    self.bal += other

  def withdraw(self, other):
    if self.bal >= other:
      self.bal -= other
    else:
      print("Insufficient funds available")

  def __str__(self):
    name = "Name: {} {}".format(self.name, self.sur)
    iban = "Account number: {}".format(self.iban)
    atype = "Account type: {}".format(self.account_type)
    balance = "Balance: {:.2f}".format(self.bal)
    return "\n".join([name, iban, atype, balance])

class CurrentAccount(BankAccount):
  overdraft = -1000
  account_type = "Current"

  def withdraw(self, other):
    if self.bal - other >= -1000:
      self.bal -= other
    else:
      print("Insufficient funds available")

  def __str__(self):
    over = "Overdraft: {:.2f}".format(self.overdraft)
    return "\n".join([super().__str__(), over])

class SavingsAccount(BankAccount):
  interest_rate = 0.01
  account_type = "Savings"

  def apply_interest(self):
    self.bal *= (1 + self.interest_rate)

  def __str__(self):
    rate = "Interest rate: {}".format(self.interest_rate)
    return "\n".join([super().__str__(), rate])

def main():
    a1 = CurrentAccount('Joe', 'Murphy', 100)
    a2 = SavingsAccount('Mandy', 'Murray', 100)
    a3 = SavingsAccount('Jimmy', 'Smith', 200)
    a4 = BankAccount('Frank', 'Wrigley', 500)

    # Print base classes
    print('Base classes...')
    print(a1.__class__.__bases__)
    print(a2.__class__.__bases__)

    # Print account details
    print('Account details...')
    print(a1)
    print(a2)
    print(a3)
    print(a4)
    print('-' * 20)

    # Call some methods
    a1.lodge(50)
    a1.withdraw(100)
    a1.withdraw(100)
    a1.withdraw(1000)
    a2.withdraw(10)
    a2.withdraw(100)
    a2.lodge(20)
    a2.apply_interest()
    a4.lodge(20)
    a4.withdraw(20)
    a4.withdraw(1000)

    # Some methods should not exist
    try:
        a1.apply_interest()
    except AttributeError:
        print('No such method')
    try:
        a4.apply_interest()
    except AttributeError:
        print('No such method')
    print('-' * 20)

    # Print account details
    print('Account details...')
    print(a1)
    print(a2)
    print(a3)
    print(a4)

if __name__ == '__main__':
   main()

