from collections import namedtuple

Student = namedtuple("Student", ["firstname", "surname", "id"])

def show_student(s):
    print("{:>s} {}".format("First name:", s[0]))
    print("{:>{}s} {}".format("Surname:", len("First name:"), s[1]))
    print("{:>{}s} {}".format("ID:", len("First name:"), s[2]))