def power(m, n):
    if n == 0:
        return 1

    n -= 1
    return m * power(m, n)

def main():
    print(power(2,3))
    print(power(4,4))
    print(power(2,32))
    print(power(10,3))
    print(power(8,0))

if __name__ == '__main__':
    main()