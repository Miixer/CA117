import sys
import math

def pi(n):
    pi = math.pi
    pi = "{:.{}f}".format(pi, n)
    return pi



def main():
    n = int(sys.argv[1])
    print(pi(n))


if __name__ == '__main__':
    main()