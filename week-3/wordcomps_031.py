import sys

def allvowels(s):
   vset = set(vowels)
   words = set(words)
   allv = [w for w in words if vset.issubset(words)]

def main():
   vowels = "aeiou"
   words = [w.strip() for w in sys.stdin]
   print(allvowels(words))
   exactly17 = [w for w in words if len(w) == 17]
   morethan17 = [w for w in words if len(w) > 17]





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