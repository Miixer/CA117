import sys

def mean(num):
   return sum(num) / len(num)

def mode(num):
   return max(num, key = num.count)

def median(num):
   num = sorted(num)
   if len(num) % 2 == 1:
      return num[int(len(num) / 2)]
   else:
      return (num[int(len(num) / 2) - 1] + num[int(len(num) / 2)]) / 2
   
def main():
   n = [int(s.strip()) for s in sys.stdin]
   print("Mean: {:.1f}".format(mean(n)))
   print("Mode: {:.1f}".format(mode(n)))
   print("Median: {:.1f}".format(median(n)))
   
if __name__ == '__main__':
   main()