def capital(s):
    first = s[0].upper()
    last = s[len(s)-1].upper()
    middle = s[1:len(s)-1]
    if len(s) > 1:
      return first + middle + last 

def main():
    import sys
    for line in sys.stdin:
        cs = capital(line.strip())
        if cs:
            print(cs)

if __name__ == '__main__':
   main()