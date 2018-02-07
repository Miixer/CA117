import sys

def diamond(n):
    d = ""
    i = 0
    while i < n:
        d = d + ((n - i - 1) * " ") + ("* " * i) + "*" + "\n"
        i = i + 1
    i = 0
    while i < n - 1:
        d = d + (" " * (i + 1)) + ("* " * (n - i - 2)) + "*" + "\n"
        i = i + 1
    return d.rstrip()

def main():
    print(diamond(int(sys.argv[1])))

if __name__ == '__main__':
    main()