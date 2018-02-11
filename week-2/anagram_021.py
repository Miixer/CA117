import sys

def anagram(left, right):
    for c in left:
        if c in right and len(left) == len(right):
            right.replace(c, "", 1)
        else:
            return False
    return True

def main():
    for line in sys.stdin:
        line = line.split()
        check = anagram(line[0], line[1])
        print(check)


if __name__ == '__main__':
    main()