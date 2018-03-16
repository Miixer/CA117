from random import randint

top = 1000000
bottom = 0
z = randint(bottom, top)

def guess(g):
    if g == z:
        return 0
    elif g < z:
        return -1
    else:
        return 1

def find():
    low = bottom
    high = top
    while True:
        mid = int((low + high) / 2)
        num = guess(mid)
        if num == -1:
            low = mid
        elif num == 1:
            high = mid
        else:
            return mid

def main():
    a = find()
    if a == z:
        print('Correct!')
    else:
        print('Incorrect!')
    print('You said {:d} and answer is {:d}'.format(a, z))

if __name__ == '__main__':
    main()