import sys

def words():
    d = {
    "0" : "zero",
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine",
    "10" : "ten"
    }
    return d

def translate(f):
    irish = {}
    for line in f:
        eng, gaeilge = line.split()
        irish[eng] = gaeilge
    return irish

def main():
    with open(sys.argv[1], "r") as f:
        irish = translate(f)

    for line in sys.stdin:
        num = line.split()
        d = words()
        s = ""
        for n in num:
            s += "{} ".format(irish[d[n]])
        print(s.strip())

if __name__ == '__main__':
    main()