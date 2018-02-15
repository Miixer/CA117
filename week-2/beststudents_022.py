import sys

def file(s):
    with open(s, "r") as f:
        return [c.strip().split() for c in f]

def checkmark(n):
    return int(n)

def main():
    s = sys.argv[1]
    try:
        words = file(s)
        students = (sorted(words))
        bestmark = max(students)[0]
        for n in words:
            try:
                marks = n[:][0]
                checkmark(marks)
            except ValueError:
                print("Invalid mark {} encountered. Skipping.".format(marks))
        for n in students:
            if 
            print(n)

    except FileNotFoundError:
        print("The file {} could not be opened.".format(s))

    finally:
        print("Best student(s): {}, {}".format("ok","ok"))
        print("Best mark: {}".format(bestmark))


if __name__ == '__main__':
    main()