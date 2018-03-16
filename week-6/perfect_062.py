import sys

def sumFac(n):
   n = int(n)
   if n == 1:
      return False
   sqrt = int(n**(0.5))
   sumf = 1
   for i in range(2, sqrt + 1):
      if n % i == 0:
         sumf += i+(n/i)
   return sumf


def isPerfect(n, sumf):
   return sumf == n

def main():
   for line in sys.stdin:
      sumf = sumFac(line)
      print(isPerfect(int(line), sumf))

if __name__ == '__main__':
   main()