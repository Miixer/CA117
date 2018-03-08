import sys

def check(word):
   s = ""
   for w in word.lower():
      for c in "aeiou":
         if w in c:
            s += w
   if s == "aeiou":
      print(word)

def main():
   for line in sys.stdin:
      line = line.strip()
      check(line)

if __name__ == '__main__':
   main()