from collections import namedtuple
Module = namedtuple('Module', 'code title ects')

CA1_MODULES = {'CA103': Module('CA103', 'Computer Systems', 5),
               'CA106': Module('CA106', 'Web Design', 5),
               'CA115': Module('CA115', 'Digital Innovation', 5),
               'CA116': Module('CA116', 'Computer Programming I', 10),
               'CA117': Module('CA117', 'Computer Programming II', 10),
               'CA169': Module('CA169', 'Networks and Internet', 5),
               'CA170': Module('CA170', 'Operating Systems', 5),
               'CA172': Module('CA172', 'Problem Solving', 5),
               'MS121': Module('MS121', 'IT Mathematics', 10)}

class Student(object):

    def __init__(self, idnum, surname, firstname):
        self.idnum = idnum
        self.surname = surname
        self.firstname = firstname
        self.mods = CA1_MODULES
        self.marks = {code: 0 for code in self.mods.keys()}

    def __str__(self):
        name = '{} : {} {}'.format(self.idnum,
                                   self.firstname,
                                   self.surname)
        uline = '-' * len(name)
        results =  '\n'.join([code + ' : ' + self.mods[code].title +
                              ' : ' + str(self.marks[code])
                              for code in sorted(self.mods.keys())])
        pm = 'Precision mark: {:.2f}'.format(self.precision_mark())
        if self.passed():
            outcome = 'Pass'
        elif self.passed_by_compensation():
            outcome = 'Pass by compensation'
        else:
            outcome = 'Fail'

        return '\n'.join([name, uline, results, pm, outcome])

    def add_mark(self, code, mark):
      self.marks[code] = int(mark)

    def precision_mark(self):
      weight = sum([self.mods[c].ects * self.marks[c] for c in self.mods])
      mark = sum(self.mods[c].ects for c in self.mods)
      return weight / mark
    
    def passed(self):
      failed = [c for c in self.marks if int(self.marks[c]) < 40]
      return len(failed) == 0

    def passed_by_compensation(self):
      if self.precision_mark() < 45:
        return False
      cred = sum([self.mods[c].ects for c in self.mods])
      credf = sum([self.mods[c].ects for c in self.mods if self.marks[c] < 40])
      if credf/cred > 1/6:
        return False
      if any([self.marks[c] < 35 for c in self.mods]):
        return False
      return True

def main():
    s1 = Student(15334499, 'Jones', 'Zoe')
    s1.add_mark('CA103', 71)
    s1.add_mark('CA106', 65)
    s1.add_mark('CA115', 84)
    s1.add_mark('CA116', 85)
    s1.add_mark('CA117', 70)
    s1.add_mark('CA169', 68)
    s1.add_mark('CA170', 74)
    s1.add_mark('CA172', 90)
    s1.add_mark('MS121', 50)
    
    s2 = Student(15667755, "Brent", "Tom")
    s2.add_mark('CA103', 55)
    s2.add_mark('CA106', 35)
    s2.add_mark('CA115', 70)
    s2.add_mark('CA116', 64)
    s2.add_mark('CA117', 66)
    s2.add_mark('CA169', 50)
    s2.add_mark('CA170', 55)
    s2.add_mark('CA172', 60)
    s2.add_mark('MS121', 35)

    s3 = Student(15112277, 'Brody', 'Joe')
    s3.add_mark('CA103', 35)
    s3.add_mark('CA106', 35)
    s3.add_mark('CA115', 60)
    s3.add_mark('CA116', 60)
    s3.add_mark('CA117', 60)
    s3.add_mark('CA169', 60)
    s3.add_mark('CA170', 60)
    s3.add_mark('CA172', 60)
    s3.add_mark('MS121', 60)

    print(s1)
    print(s2)
    print(s3)

if __name__ == '__main__':
  main()