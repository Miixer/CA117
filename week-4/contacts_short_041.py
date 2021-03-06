import sys

def check(n,d):
   print("Name: {}".format(n))
   if n in d:
      print("Phone: {}".format(d[n]))
   else:
      print("No such contact")

      
def main():
   contacts = {}
   with open(sys.argv[1]) as f:
      for line in f:
         name, number = line.strip().split()
         contacts[name] = number
      
   for name in sys.stdin:
      check(name.strip(),contacts)
   
      

if __name__ == '__main__':
   main()