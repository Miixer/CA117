import sys

s = sys.argv[1]

def prime(x):
   if x >= 2:
      for y in range(2,x):
         if not (x % y):
            return False
   else:
      return False
   return True



def main():
   l = [n for n in range(1, int(s) + 1)]
   m3 = [n for n in l if not n % 3]
   m4 = [n for n in l if not n % 4]
   m3sq = [n ** 2 for n in m3]
   m4d = [n * 2 for n in l if not n % 4]
   m3orm4 = [n for n in l if n in m3 or n in m4]
   m3andm4 = [n for n in l if n in m3 and n in m4]
   m3x = ["X" if n in m3 else n for n in l]
   primes = [n for n in l if prime(n)]

   print("Multiples of 3:", m3)
   print("Multiples of 3 squared:", m3sq)
   print("Multiples of 4 doubled:", m4d)
   print("Multiples of 3 or 4:", m3orm4)
   print("Multiples of 3 and 4:", m3andm4)
   print("Multiples of 3 replaced:", m3x)
   print("Primes:", primes)


if __name__ == '__main__':
   main()