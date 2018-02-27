import sys, string

def main():
    count = {}
    unique = []
    for line in sys.stdin:
        line = line.strip().split()
        for w in line:
            w = w.strip(string.punctuation).lower()
            unique.append(w)
            if w in count:
                count[w] += 1
            else:
                count[w] = 1

    unique = sorted(set(unique))
    for c in unique:
        print("{} : {}".format(c, count[c]))

if __name__ == '__main__':
    main()