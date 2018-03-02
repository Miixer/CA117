import sys

def mean(line):
   pass
   
def main():
   for c in sys.stdin:
      l = [c for c in sys.stdin]
      print(l)
      n = [int(x) for x in l]
      print(sum(n) / len(n))
   
if __name__ == '__main__':
   main()