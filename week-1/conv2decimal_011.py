import sys

def convert(n, base):
    new = int(n, base)
    return new

def main():
    for line in sys.stdin:
        [n, base] = line.strip().split()
        base = int(base)
        nint = convert(n, base)
        print(nint)

if __name__ == '__main__':
    main()
