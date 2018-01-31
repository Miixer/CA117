import sys

def contains(chars, s):
    for c in chars:
        if c in s:
            s = s.replace(c, '')
        else:
            return False
    return True


def main():
    for line in sys.stdin:
        line = line.strip().lower().split()
        result = contains(line[0], line[1])
        print(result)


if __name__ == '__main__':
    main()