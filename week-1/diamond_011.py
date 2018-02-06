import sys


def main():
    n = int(sys.argv[1])
    for x in list(range(n)) + list(reversed(range(n - 1))):
        print('{: <{w1}}{:*<{w2}}'.format('','', w1=n-x-1, w2=x*2+1))

if __name__ == '__main__':
    main()

