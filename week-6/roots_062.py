import sys
import math

def quadratic(a,b,c):
   try:
      r1 = (-b + math.sqrt(b**2-(4*a*c)))*1/(2*a)
      r2 = (-b - math.sqrt(b**2-(4*a*c)))*1/(2*a)
      roots = ("r1 = {}, r2 = {}").format(r1,r2)
      return roots
   except:
      return None

def main():
   co = [c.strip().split() for c in sys.stdin]
   for c in co:
      a,b,c = int(c[0]), int(c[1]), int(c[2])
      print(quadratic(a,b,c))
   
if __name__ == '__main__':
   main()