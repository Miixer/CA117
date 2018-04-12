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


def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)

    tn.add(t1)
    tn.add(t2)

    t = tn.lookup(21)
    assert(isinstance(t, Triathlete))
    assert(t.name == 'Ian Brown')
    assert(t.tid == 21)
    
    tn.remove(21)
    t = tn.lookup(21)
    assert(t is None)

if __name__ == '__main__':
    main()