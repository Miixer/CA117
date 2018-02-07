import sys

def name(s):
    n = " ".join(s[1:-8])
    return n


def main():
    
    lines = []
    longest = 0
    for line in sys.stdin:
        line = line.split()
        lines.append(line)
        n = name(line)
        if len(n) > longest:
            longest = len(n)

    h1 = "POS"
    h2 = "CLUB"
    h3 = "P"
    h4 = "W"
    h5 = "D"
    h6 = "L"
    h7 = "GF"
    h8 = "GA"
    h9 = "GD"
    h10 = "PTS"

    print('{:>s} {:<{}s} {:>2s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s}'.format(h1, h2, len(n), h3, h4, h5, h6, h7, h8, h9, h10))
    
    print(lines)

    
    
       
    


if __name__ == '__main__':
    main()