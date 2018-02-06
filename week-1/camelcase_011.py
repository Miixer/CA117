import sys

def capitalise(s):
    s = ''.join(c for c in s.title())
    return s

def main():
    for line in sys.stdin:
        s = line.strip()
        camel = capitalise(s)
        print(camel)

if __name__ == '__main__':
    main()