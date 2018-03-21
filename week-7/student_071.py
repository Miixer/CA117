class Student(object):

    def __init__(self, surname, forename, sid, modlist=None):
        self.id = sid
        self.sur = surname
        self.name = forename
        if modlist == None:
            modlist = []
        self.mod = modlist

    def add_module(self, new):
        self.mod.append(new)

    def del_module(self, old):
        if old in self.mod:
            self.mod.pop(self.mod.index(old))

    def print_details(self):
        print("ID: {}".format(self.id))
        print("Surname: {}".format(self.sur))
        print("Forename: {}".format(self.name))
        print("Modules: {}".format(" ".join(self.mod)))

def main():

    student1 = Student('Murphy', 'Jimmy', 15234654)
    student1.add_module('CA117')
    student1.add_module('CA116')
    student1.add_module('CA114')
    student1.print_details()
    
    student2 = Student('Lannister', 'Cersei', 15876123, ['CA115', 'CA216'])
    student2.del_module('CA216')
    student2.del_module('CA117')
    student2.del_module('CA216')
    student2.add_module('CA117')
    student2.print_details()

if __name__ == '__main__':
    main()