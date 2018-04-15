class Triathlete(object):

    def __init__(self, name, tid):
        self.name = name
        self.tid = tid
        self.d = {}

    def add_time(self, disc, time):
        self.d[disc] = time
        return self.d

    def get_time(self, disc):
        return self.d[disc]

    def total_time(self):
        return sum(self.d.values())

    def __eq__(self, other):
        return self.total_time() == other.total_time()

    def __gt__(self, other):
        return self.total_time() > other.total_time()

    def __lt__(self, other):
        return self.total_time() < other.total_time()

    def __str__(self):
        return ("Name: {}\nID: {}\nRace time: {}".format(self.name, self.tid, self.total_time()))
        


class Triathlon(object):

    def __init__(self):
        self.d = {}

    def add(self, other):
        self.d[other.tid] = other

    def remove(self, other):
        del self.d[other]
        return self.d

    def lookup(self, other):
        try:
            return self.d[other]
        except KeyError:
            return None

    def sort(self):
        l = []
        for k in self.d:
            l.append([self.d[k].name, self.d[k].tid])
        s = []
        for c in sorted(l):
            s.append("Name: {}".format(c[0]))
            s.append("ID: {}".format(c[1]))
        return s

    def __str__(self):
        return "\n".join(self.sort())

def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('Alan Wren', 23)

    tn.add(t1)
    tn.add(t2)
    tn.add(t3)

    print(tn)

if __name__ == '__main__':
    main()