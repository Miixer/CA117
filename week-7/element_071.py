class Element(object):

    def __init__(self, number, name, symbol, boling_point):
        self.num = number
        self.name = name
        self.symbol = symbol
        self.boil = boling_point

    def print_details(self):
        print("Number: {}".format(self.num))
        print("Name: {}".format(self.name))
        print("Symbol: {}".format(self.symbol))
        print("Boiling point: {} K".format(self.boil))

def main():

    e1 = Element(1, 'Hydrogen', 'H', 20.3)
    e2 = Element(3, 'Lithium', 'Li', 1615)
    e3 = Element(11, 'Sodium', 'Na', 1156)
    e4 = Element(12, 'Magnesium', 'Mg', 1380)
    e5 = Element(79, 'Gold', 'Au', 3129)

    e1.print_details()
    e2.print_details()
    e3.print_details()
    e4.print_details()
    e5.print_details()

if __name__ == '__main__':
    main()