import sys

def grades(marks, names):
    c = []
    highest = 0
    i = 0
    while i < len(marks):
        if int(marks[i]) > int(highest):
            highest = marks[i]
        i = i + 1
    i = 0
    while i < len(marks):
        if marks[i] == highest:
            c.append(names[i].strip())
        i = i + 1
    best = ", ".join(c)

    print("Best student(s): {}".format(best))
    print("Best mark: {}".format(highest))

def main():
    s = sys.argv[1]
    marks = []
    names = []
    try:
        with open(s, "r") as f:
            for line in f:
                try:
                    if line[:2].isdigit():
                        marks.append(line[:2])
                except ValueError:
                    print('Invalid mark {} encountered. Skipping.'.format(line[:2]))
                names.append(line[2:])
            grades(marks, names)
    except FileNotFoundError:
        print('The file {} could not be opened'.format(s))

if __name__ == '__main__':
    main()
