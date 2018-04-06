from stack_092 import Stack
import sys, math, operator

s = Stack()
d = {
        "+" : operator.add,
        "-" : operator.sub,
        "*" : operator.mul,
        "/" : operator.truediv,
        "r" : math.sqrt,
        "n" : operator.neg,
    }

def calculator(line):
    
    line = line.split()
    num = []
    for c in line:
        if not c in "+-*/rn":
            s.push(float(c))
            num.append(c)
        else:
            if c in "+-*/":
                n1 = s.pop()
                n2 = s.pop()
                s.push(d[c](n2, n1))
            else:
                n = s.pop()
                s.push(d[c](n))
    return s.pop()

def main():

    for line in sys.stdin:
        try:
            a = calculator(line.strip())
            print('{:.2f}'.format(a))
        except IndexError:
            print('Invalid RPN expression')

if __name__ == '__main__':
    main()