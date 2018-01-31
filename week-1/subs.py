import sys
for line in sys.stdin:
    [left, right] = line.strip().split()
    #print(line)
    print(left[1], right[0])