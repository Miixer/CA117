import sys

def file(s):
    with open(s, "r") as f:
        return [c.strip().split() for c in f]

def checkmark(n):
    pass

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
                if marks.isdigit():
                    marks = marks
            except ValueError:
                print("Invalid mark {} encountered. Exiting.".format(marks))            

    except FileNotFoundError:
        print("The file {} could not be opened.".format(s))

            

if __name__ == '__main__':
    main()