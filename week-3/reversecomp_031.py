import sys

def main():
    l = set()
    x = set()
    ans = []
    words = [w.strip() for w in sys.stdin]
    for w in words:
        if len(w) >= 5:
            l.add(w)
    for w in l:
        s = w
        w = w[::-1].lower()
        if w in l or w.capitalize() in l:
            x.add(s)
    for s in x:
        ans.append(s)
    ans = sorted(ans, key=str.lower)
    print(ans)


if __name__ == '__main__':
    main()