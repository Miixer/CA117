import sys

def crazy(s):
    s = ' '.join(c[:-1] + c[len(c) - 1].title() for c in s.split())
    return s

def main():
    for line in sys.stdin:
        s = line.strip()
        camel = crazy(s)
        print(camel)

if __name__ == '__main__':
    main()