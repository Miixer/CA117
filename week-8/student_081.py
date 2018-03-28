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
      pmark = 0
      tc = 0
      for c in self.marks:
        tc += int(self.mods[c][2])
        pmark += int(self.mods[c][2]) * (self.marks[c] / 100)
      return (pmark / tc) * 100
    def passed(self):
      failed = [c for c in self.marks if int(self.marks[c]) < 40]
      return len(failed) == 0
    def passed_by_compensation(self):
      if self.precision_mark() < 45:
        return False
      failed = [c for c in self.marks if int(self.marks[code]) < 40]
      cf = 0
      tc = 0
      for c in self.mods:
        tc += int(self.mods[code][2])
        if code in failed:
          cf += int(self.mods[code][2])
      if (cf * 6) > tc:
        return False
      tfail = [c for c in self.marks if int(self.marks[code]) < 35]
      return not len(tfail)

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
    print(s1)

if __name__ == '__main__':
  main()