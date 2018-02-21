import sys

def allvowels(l):
   vowels = "aeiou"
   vset = set(vowels)
   l = set(l)
   allv = [w for w in l if vset.issubset(w)]
   return min(allv, key=len)

def four_as(l):
   a = "a"
   four_a = []
   for word in l:
      count = 0
      for i in range(len(word)):
         if word[i].lower() == a:
            count += 1
      if count == 4:
         four_a.append(word)
   return four_a

def qs(l):
   q = "q"
   ans = []
   for word in l:
      count = 0
      for i in range(len(word)):
         if word[i].lower() == q:
            count += 1
      if count == 2:
         ans.append(word)
   return ans

def cie(l):
   c = "cie"
   ans = []
   for word in l:
      count = 0
      for i in range(len(word)):
         if word[i].lower() == c:
            count += 1
   return ans

def main():
   words = [w.strip() for w in sys.stdin]
   exactly17 = [w for w in words if len(w) == 17]
   morethan17 = [w for w in words if len(w) > 17]
   print(allvowels(words))
   print(four_as(words))
   print(qs(words))
   print(cie(words))






if __name__ == '__main__':
   main()

# vset(vowels)
# l = set(l)
# all_vowels=[w for w in l if vset.issubset(w)]
# return min(all_vowels, key=len)


# foura
# a = ["a","a","a","a"]
# a = set(a)
# l = set(l)
# four_a = [word for word in l if a.issubset(word)]
# return