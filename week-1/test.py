import sys


def main():
    
    lines = []
    longest = 0
    for line in sys.stdin:
        line = line.strip()
        lines.append(line)
        if longest < len(" ".join(line.split()[1:-8])):
            longest = len(" ".join(line.split()[1:-8]))

    print('{:>s} {:<{}s} {:s} {:s} {:s} {:s} {:s} {:s} {:s} {:s}'.format("POS", "CLUB", longest, " P", "  W", "  D", "  L", " GF", " GA", " GD", "PTS"))
    
    for line in lines:
        line = line.split()
        team_name = line[1:-8]
        print("{:>3s} {:<{}s} {:s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s} {:>3s})".format(line[0], " ".join(team_name), longest, line[-8], line[-7], line[-6], line[-5], line[-4], line[-3], line[-2], line[-1]))

if __name__ == '__main__':
    main()