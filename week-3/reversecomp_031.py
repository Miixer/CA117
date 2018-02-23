import sys

# def main():
#     l = []
#     ans = []
#     words = [w.strip() for w in sys.stdin]
#     for w in words:
#         if len(w) >= 5:
#             x = w[::-1]
#             l.append(w)
#     print(l)
#     for w in l:
#         if w == x:
#             print(w)

def main():
    ans = []
    l = set()
    words = [w.strip() for w in sys.stdin]
    for w in words:
        if len(w) >= 5:
            l.add(w)
    s = w
    for c in l:
        low = c.lower()
        low = c[::-1]
        cap = c.capitalize()
        if low in l or cap in l:
            ans.append(s)

    for s in ans:
        ans.append(w)
    ans = sorted(ans, key=str.lower)
    print(ans)

# def main():
#     s = sys.stdin.readlines()
#     a = set()
#     p = set()
#     r = []
#     for line in s:
#         if len(line.strip()) >= 5:
#             a.add(line.strip())
#     for c in a:
#         f = c
#         c = c.lower()
#         c = c[::-1]
#         d = c.capitalize()
#         if c in a or d in a:
#                 p.add(f)
#     for f in p:
#         r.append(f)
#     r = sorted(r, key=str.lower)
#     print (r)

if __name__ == '__main__':
    main()