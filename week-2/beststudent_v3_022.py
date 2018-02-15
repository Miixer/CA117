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
        best = 0
        student = (max(words))
        name = " ".join(student[1:])
        grade = student[0]
        for n in words:
            try:
                marks = n[:][0]
                checkmark(marks)
            except ValueError:
                print("Invalid mark {} encountered. Skipping.".format(marks))

    except FileNotFoundError:
        print("The file {} could not be opened.".format(s))

    finally:
        print("Best student: {}".format(name))
        print("Best mark: {}".format(grade))


if __name__ == '__main__':
    main()