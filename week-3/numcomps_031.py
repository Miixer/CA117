import sys

s = sys.argv[1]
# for n in range(1,int(s)):
#    print(n)

l = [n for n in range(1,int(s)+1)]

m3 = [n for n in l if not n%3]
print(m3)

sq = [n**2 for n in m3]
print(sq)

dm4 = [n*2 for n in l if not n%4]
print(dm4)

m3or4 = [n if not n%3 or n if not n%4 for n in l]