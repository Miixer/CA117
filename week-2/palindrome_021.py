import sys
import string

def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False


def main():
    for line in sys.stdin:
        line = line.casefold().strip()
        table = line.maketrans({key: None for key in string.punctuation})
        new = line.translate(table).replace(" ", "")
        print(palindrome(new))

if __name__ == '__main__':
    main()