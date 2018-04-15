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

    def sort(self):
        l = []
        for k in self.d:
            l.append([self.d[k].total_time(), self.d[k].tid])
        return l

    def best(self):
        return self.d[min(self.sort())[1]]

    def worst(self):
        return self.d[max(self.sort())[1]]

    def __str__(self):
        return "\n".join(self.sort())

def main():

    tn = Triathlon()
    t1 = Triathlete('Ian Brown', 21)
    t2 = Triathlete('John Squire', 22)
    t3 = Triathlete('Alan Wren', 23)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    t2.add_time('swim', 300)
    t2.add_time('cycle', 100)
    t2.add_time('run', 200)

    t3.add_time('swim', 50)
    t3.add_time('cycle', 20)
    t3.add_time('run', 10)
    
    tn.add(t1)
    tn.add(t2)
    tn.add(t3)

    print(tn.best())
    print(tn.worst())

if __name__ == '__main__':
    main()