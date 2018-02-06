import sys
import string

def main():
    for line in sys.stdin:
        line = line.strip()
        upper = 0
        lower = 0
        digit = 0
        special = 0
        for s in line:
            if s.isdigit() and digit == 0:
                digit =+ 1
            elif s.isupper() and upper == 0:
                upper =+ 1
            elif s.islower() and lower == 0:
                lower =+ 1
            elif s in string.punctuation and special == 0:
                special =+ 1
        print(digit + upper + lower + special)

if __name__ == '__main__':
    main()