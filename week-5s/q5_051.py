import sys

def main():
   info = [line.strip().replace(":", "") for line in sys.stdin]
   for n in info:
      try:
         mintimes = []
         names = n.split()[0]
         times = n.split()[1:]
         mintimes.append(min(sorted(times), key=int))
         print("".join(str(mintimes).strip()))
      except ValueError:
         continue

if __name__ == '__main__':
   main()