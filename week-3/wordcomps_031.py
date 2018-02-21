import sys

def exactly17(l):
   return [w for w in l if len(w) == 17]

def morethan17(l): 
   return [w for w in l if len(w) > 17]

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
   ans = []
   for word in l:
      count = 0
      for i in range(len(word)):
         if word[i].lower() == "q":
            count += 1
      if count == 2:
         ans.append(word)
   return ans

def cie(l):
   c = "cie"
   ans = []
   for word in l:
      if c.lower() in word:
         ans.append(word)
   return ans

def anagram(l):
   s = 'angle'
   ans = [c for c in l if sorted(c.lower()) == sorted(s)]
   ans.remove(s)
   return ans

def iary(l):
   c = "iary"
   return [c for word in l if c.lower() in word[-4:]]

def qnou(l):
   return [word for word in l if "q" in word.lower() and "qu" not in word.lower()]

def most(l):
   e = "e"
   most = []
   e_words = [w for w in l if e in w]
   count = 0
   for word in e_words:
      check = 0
      for i in range(len(word)):
         if e in word[i]:
            check += 1
      if check > count:
         count = check

   for word in e_words:
      check = 0
      for i in range(len(word)):
         if word[i].lower() == e:
            check += 1
      if check == count:
         most.append(word)
   return most

def main():
   words = [w.strip() for w in sys.stdin]
   print("Words containing 17 letters: {}".format(exactly17(words))) 
   print("Words containing 18+ letters: {}".format(morethan17(words)))
   print("Shortest word containing all vowels: {}".format(allvowels(words)))
   print("Words with 4 a's: {}".format(four_as(words)))
   print("Words with 2+ q's: {}".format(qs(words)))
   print("Words containing cie: {}".format(cie(words)))
   print("Anagrams of angle: {}".format(anagram(words)))
   print("Words ending in iary: {}".format(len(iary(words))))
   print("Words with q but no u: {}".format(qnou(words)))
   print("Words with most e's: {}".format(most(words)))


if __name__ == '__main__':
   main()


