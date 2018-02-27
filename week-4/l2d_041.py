def l2d(s):
    l = []
    d = {}
    for line in s:
        l.append(line.strip())
    animals, numbers = l[0].split(), l[1].split()
    for a,n in zip(animals, numbers):
        d[a] = n
    return d