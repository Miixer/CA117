import sys

def calories(s):
    cals = {}
    with open(s, "r") as f:
        for line in f:
            info = line.strip().split()
            name, num = " ".join(info[:-1]), int(info[-1])
            cals[name] = num
    return cals

def totalcals(line, cals):
    total = 0
    name, food = line[0], line[1:]
    for f in food:
            if f in cals:
                total += cals[f]
            else:
                total += 100
    return name, total

def main():
    cals = calories(sys.argv[1])
    totalname = {}
    for line in sys.stdin:
        line = line.strip().split(",")
        name, total = totalcals(line, cals)
        totalname[name] = total
    namelen = len(max(totalname.keys(), key=len))
    totalen = len(str(max(totalname.values())))

    for k,v in sorted(totalname.items(), key = lambda x: x[1]):
        print("{:>{}s} : {:>{}d}".format(k, namelen, v, totalen))

if __name__ == '__main__':
    main()