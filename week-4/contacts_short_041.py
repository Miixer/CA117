import sys

def file(s):
   d = {}
   with open(s, "r") as f:
      for w in f:
         w = w.strip().split()
         d[w[0]] = w[1]
   return d
      
def main():
   d = file(sys.argv[1])
   for line in sys.stdin:
      names = line.strip().split()
   for k,v in d.items():
      for v in names:
         #print(k)
         if k in d.keys():
            print(k)
         else:
            print("no")

      

if __name__ == '__main__':
   main()