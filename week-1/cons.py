import sys

def main():
    for line in sys.stdin:
        status = True
        [chars, string] = line.strip().lower().split()
        for c in chars:
            if c in string:
                string = string.replace(c, '')
            else:
                status = False
        print(status)

if __name__ == '__main__':
    main()