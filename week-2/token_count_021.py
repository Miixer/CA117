import sys

def main():
    lines = []
    newlist = []
    for line in sys.stdin:
        line = line.strip().split()
        lines.append(line)
        lines = [x for x in lines if x]
        newlist = sum(lines, [])
    print(len(newlist))

if __name__ == '__main__':
    main()