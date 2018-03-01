import sys

def vowelcount(c):
    count = {}
    vowels = "aeiou"
    for v in vowels:
        count[v] = c.count(v)
    return count

def main():
    num = []
    nkeys = {}
    text = sys.stdin.read().lower()
    count = vowelcount(text)
    for key in count:
        num.append(count[key])
        nkeys[count[key]] = key
    num = sorted(num, reverse=True)
    for n in num:
        print("{} : {:>{}d}".format(nkeys[n], n, len(str(max(num)))))
    

if __name__ == '__main__':
    main()