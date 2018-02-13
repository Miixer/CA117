import sys


def file(s):
    pass


def main():
    s = sys.argv[1]
    try:
        best = 0
        with open(s, "r") as f:
            words = [c.strip().split() for c in f]
            print(words)

    except FileNotFoundError:
        print("The file {} could not be opened.".format(s))        

if __name__ == '__main__':
    main()