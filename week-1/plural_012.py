import sys

es_endings = ["ch", "sh", "x", "s", "z", "o"]
vowels = "aeiou"

def plural(s):
    if s[-2:] in es_endings or s[-1] in es_endings:
        s = s + "es"
    elif s[-1] == "y" and s[-2] not in vowels:
        s = s[:-1] + "ies"
    elif s[-1] == "f" or s[-2:] == "fe":
        s = s.split("f", 1)[0] + "ves"
    else:
        s = s + "s"
    return s

def main():
    for line in sys.stdin:
        word = plural(line.strip())
        print(word)

if __name__ == '__main__':
    main()