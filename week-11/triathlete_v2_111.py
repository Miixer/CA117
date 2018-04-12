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

    def __str__(self):
        return ("Name: {}\nID: {}\nRace time: {}".format(self.name, self.tid, self.total_time()))


def main():

    t1 = Triathlete('Ian Brown', 21)

    t1.add_time('swim', 100)
    t1.add_time('cycle', 120)
    t1.add_time('run', 150)

    print('Cycle: {}'.format(t1.get_time('cycle')))
    print(t1)

if __name__ == '__main__':
    main()