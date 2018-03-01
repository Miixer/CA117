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
    ans = [w for w in unique if len(w) > 3 and count[w] >= 3]
    for c in ans:
        print("{:>{}s} : {:>2n}".format(c, len(max(ans, key=len)), count[c]))

if __name__ == '__main__':
    main()