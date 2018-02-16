import sys

def main():
   for line in sys.stdin:
      line = line.split()
      for w in line:
        try:
            print("Thank you for", int(w)) 
            return w          
        except ValueError:
            print(w, "is not a number")

if __name__ == '__main__':
   main()