from stack_092 import Stack
import sys

def matcher(line):

    par = Stack()
    cur = Stack()
    sqr = Stack()
    d = {"(" : par, ")" : par, "{" : cur, "}" : cur, "[" : sqr, "]" : sqr}
    l = ["(", "{", "["]
    for i in range(0, len(line)):
        if line[i] in l:
            d[line[i]].push(line[i])
        else:
            try:
                result = d[line[i]].pop()
            except:
                return False
    return not len(par) + len(cur) + len(sqr)

def main():

    for line in sys.stdin:
        print(matcher(line.strip()))

if __name__ == '__main__':
    main()
