import sys
from l2d_041 import l2d
# def l2d(s):
#     l = []
#     d = {}
#     for line in s:
#         l.append(line.strip())
#     animals, numbers = l[0].split(), l[1].split()
#     for a,n in zip(animals, numbers):
#         d[a] = n
#     return d

def main():
    d = l2d(sys.stdin)
    for (k, v) in sorted(d.items()):
        print("{} : {}".format(k, v))

if __name__ == '__main__':
    main()
    