import sys

def main():
   l = [c.strip() for c in sys.argv[1:]]
   word, num = l[0], int(l[1])
   ans = [""] * len(word)
   for i in range(len(word)):
      pos = i + num
      ans[pos % len(word)] = word[i]
   print("".join(ans))

   
if __name__ == '__main__':
   main()