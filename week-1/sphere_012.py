import sys
import math

def area(r):
    a = (4 * math.pi) * (r ** 2)
    return a

def volume(r):
    v = (4/3 * math.pi) * (r ** 3)
    return v

def main():
    start = float(sys.argv[1])
    inc = float(sys.argv[2])
    stop = float(sys.argv[3])
    
    h1 = "Radius (m)"
    h4 = "-" * len(h1)
    h2 = "Area (m^2)"
    h5 = "-" * len(h2)
    h3 = "Volume (m^3)"
    h6 = "-" * len(h3)

    print('{:>s} {:>15s} {:>15s}'.format(h1, h2, h3))
    print('{:>s} {:>15s} {:>15s}'.format(h4, h5, h6))


    while start < inc + stop:
        print("{:10.1f} {:15.2f} {:15.2f}".format(start, area(start), volume(start)))
        start = start + inc

if __name__ == '__main__':
    main()
