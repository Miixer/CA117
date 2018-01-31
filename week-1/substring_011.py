import sys


def substring(left, right):
    if left.lower() in right.lower():
        return True
    else:
        return False


def main():
    for line in sys.stdin:
        [left, right] = line.strip().split()
        result = substring(left, right)
        print(result)



if __name__ == '__main__':
    main()