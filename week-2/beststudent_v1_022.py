import sys

def file(s):
    with open(s, "r") as f:
        return [c.strip().split() for c in f]

def main():
    s = sys.argv[1]
    try:
        words = file(s)
        student = (max(words))
        name = " ".join(student[1:])
        grade = student[0]
        print("Best student: {}".format(name))
        print("Best mark: {}".format(grade))



    except FileNotFoundError:
        print("The file {} could not be opened.".format(s))        

if __name__ == '__main__':
    main()