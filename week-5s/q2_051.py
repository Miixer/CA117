import sys

def check(word):
   s = ""
   for l in "evil":
      if word.lower().count(l) != 1:
         return False
   for l in word.lower():
      for c in "evil":
         if l in c:
            s += l
   if s == "evil":
      print(word) 

def main():
   for w in sys.stdin:
      w = w.strip()
      check(w)

if __name__ == '__main__':
   main()