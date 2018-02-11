import sys
import calendar

days = {
    0 : "Monday",
    1 : "Tuesday",
    2 : "Wednesday",
    3 : "Thursday",
    4 : "Friday",
    5 : "Saturday",
    6 : "Sunday",
}

poem = {
    0 : "Monday's child is fair of face",
    1 : "Tuesday's child is full of grace",
    2 : "Wednesday's child is full of woe",
    3 : "Thursday's child has far to go",
    4 : "Friday's child is loving and giving",
    5 : "Saturday's child works hard for a living",
    6 : "Sunday's child is fair and wise and good in every way",
}

def weekday(a, b, c):
    return calendar.weekday(c, b, a)

def birthday(s):
    print("You were born on a {} and {}.".format(days[s], poem[s]))
    return

def main():
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
    day = weekday(a, b, c)
    birthday(day)

if __name__ == '__main__':
    main()