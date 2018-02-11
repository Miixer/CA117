import sys
import string

def uniquecount(l):
    return len(set(l))

def main():
    lines = []
    newlist = []
    for line in sys.stdin:
        for c in string.punctuation:
            line = line.replace(c,"")
        line = line.lower().split()
        lines.append(line)
        newlist = sum(lines, [])
        unique = uniquecount(newlist)
    print(unique)

if __name__ == '__main__':
    main()