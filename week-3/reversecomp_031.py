import sys

def main():
    l = []
    ok = []
    words = [w.strip() for w in sys.stdin]
    for w in words:
        if len(w) >= 5:
            l.append(w)

    for w in l:
        if w.lower()[::-1] in l or w.lower() == w.lower()[::-1] or w.lower():
            ok.append(w)
    print(ok)



if __name__ == '__main__':
    main()