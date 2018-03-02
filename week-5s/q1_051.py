import sys

def main():
   s = sys.argv[1].strip()
   new = [s[i:i+2][::-1] for i in range(0, len(s), 2)]
   print("".join(new))

if __name__ == '__main__':
   main()