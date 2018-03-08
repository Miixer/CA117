import sys

def build_dictionary(filename):
   info = []
   d = {}
   for line in filename:
      info.append(line.strip())
      print(info)
      word, amount = line.strip().split()
      x = {word: amount for word, amount in line}
   #print(x)
   # for line in filename:
   #    line = line.strip().split()
   #    print(line)
   #    d[line[0]] = line[1]
   # print(d)

def main():
   build_dictionary(sys.stdin)


if __name__ == '__main__':
   main()