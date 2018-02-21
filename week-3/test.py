import sys
import stutuple_031 as stutuple


def show_student(s):
    print("{:>s} {}".format("First name:", s[0]))
    print("{:>{}s} {}".format("Surname:", len("First name:"), s[1]))
    print("{:>{}s} {}".format("ID:", len("First name:"), s[2]))


def main():
    student1 = stutuple.Student('Joe', 'Mannion', 98365338)
    student2 = stutuple.Student('Louise', 'Callaghan', 99324761)
    student3 = stutuple.Student(firstname='Noel', id=99071239, surname='Rooney')
    stulist = [student1, student2, student3]
    for s in stulist:
        show_student(s)

if __name__ == '__main__':
    main()