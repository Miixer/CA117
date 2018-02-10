import sys

def main():
    for line in sys.stdin:
        line = line.strip()
        for line in line[1]:
            print(line)

if __name__ == '__main__':
    main()