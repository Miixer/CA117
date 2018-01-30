def middle(s):
    mid = s[len(s) // 2]
    if len(s) >= 2 and len(s) % 2 != 0:
        return mid
    else:
        print('No middle character!')

def main():
    import sys
    for line in sys.stdin:
        mids = middle(line.strip())
        if mids:
            print(mids)

if __name__ == '__main__':
    main()