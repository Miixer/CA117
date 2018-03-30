class Customer(object):

   discount = 0

   def __init__(self, name, balance, addr1, addr2, addr3):
      self.name = name
      self.bal = balance
      self.addr1 = addr1
      self.addr2 = addr2
      self.addr3 = addr3

   def owes(self):
      self.bal *= (1 - self.discount)
      return self.bal

   def __str__(self):
      info = []
      info.append("{}".format(self.name))
      info.append("{}".format(self.addr1))
      info.append("{}".format(self.addr2))
      info.append("{}".format(self.addr3))
      info.append("Balance: {:.2f}".format(self.bal))
      info.append("Discount: {:.0f}%".format(self.discount*100))
      info.append("Amount due: {:.2f}".format(self.owes()))
      return "\n".join(info)

class ValuedCustomer(Customer):
   discount = 0.1


def main():

    c1 = Customer('Jimmy', 100, '22 Main Street', 'Naas', 'Kildare');
    c2 = ValuedCustomer('Lucy', 100, '23 Main Street', 'Roosky', 'Roscommon');
    c3 = Customer('Fred', 200, '24 Main Street', 'Sneem', 'Kerry');

    print(c1)
    print(c2)
    print(c3)

if __name__ == '__main__':
   main()