import sys

def check(n,d):
   print("Name: {}".format(n))
   if n in d:
      print("Phone: {}".format(d[n][0]))
      print("Email: {}".format(d[n][1]))
   else:
      print("No such contact")

      
def main():
   contacts = {}
   with open(sys.argv[1]) as f:
      for line in f:
         line = line.strip().split()
         name, details = line[0], line[1:]
         contacts[name] = details
      
   for name in sys.stdin:
      check(name.strip(), contacts)
   
      

if __name__ == '__main__':
   main()