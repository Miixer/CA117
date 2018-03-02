import sys

def caps(word):
   cap = []
   s = ""
   for l in word:
      if l.isupper():
         s += l
      elif s != "":
         cap.append(s)
         s = ""
   if s != "":
      cap.append(s)

   print(max(cap, key=len))
def main():
   for line in sys.stdin:
      caps(line.strip())
      

if __name__ == '__main__':
   main()