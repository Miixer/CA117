import sys

def numbers():
    single = {
    "0" : "zero",
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four",
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine",
    }
    
    double = {
    "2" : "twenty",
    "3" : "thirty",
    "4" : "forty",
    "5" : "fifty",
    "6" : "sixty",
    "7" : "seventy",
    "8" : "eighty",
    "9" : "ninety"
    }

    other = {
    "10" : "ten",
    "11" : "eleven",
    "12" : "twelve",
    "13" : "thirteen",
    "14" : "fourteen",
    "15" : "fifteen",
    "16" : "sixteen",
    "17" : "seventeen",
    "18" : "eighteen",
    "19" : "nineteen",
    "100" : "one hundred"
    }

    return (single, double, other)

def main():
    for line in sys.stdin:
        num = line.split()
        single, double, other = numbers()
        s = ""
        for n in num:
            if len(n) == 1:
                s += "{} ".format(single[n])
            elif len(n) == 2 and n[1] == "0":
                s += "{} ".format(double[n[0]])
            elif n in other:
                s += "{} ".format(other[n])
            else:
                s += "{}-{} ".format(double[n[0]],single[n[1]])
        print(s.strip())

if __name__ == '__main__':
    main()