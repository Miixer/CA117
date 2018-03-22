import sys

# def longest(s1, s2):
#    shortest, longest = min([s1, s2], key = len), max([s1, s2], key = len)
#    if len(shortest) == len(longest):
#       shortest = s1
#       longest = s2
#    maxsub = 0
#    sub = ""
#    i = 0
#    while i < len(shortest):
#       if shortest[i] in longest:
#          j = i + 2
#          while j <= len(shortest) and shortest[i:j] in longest:
#             j += 1

#          if len(shortest[i:j-1]) > maxsub:
#             sub = shortest[i:j-1]
#             maxsub = len(sub)
#       i += 1

#    return sub

# def biggest(s1, s2):
#    sub = longest(s1, s2)
#    x = s2.split(sub)
#    i = len(x[0])
#    return sub, len(sub), i

def lcs(s1, s2):
   m = len(s1)
   n = len(s2)
   count = [[0] * (n + 1) for x in range(m + 1)]
   longest = 0
   lcs_set = set()
   for i in range(m):
      for j in range(n):
         if s1[i] == s2[j]:
            c = count[i][j] + 1
            count[i+1][j+1] = c
            if c > longest:
               lcs_set = set()
               longest = c
               lcs_set.add(s1[i-c+1:i+1])
            elif c == longest:
               lcs_set.add(s1[i-c+1:i+1])
   return lcs_set

def main():
   lines = [s1.strip() for s1 in sys.stdin]
   s1, s2 = lines[0], lines[1]
   sub = "".join(lcs(s1,s2))
   print("{} {} {}".format(sub, len(sub), s2.find(sub)))
   


if __name__ == '__main__':
   main()