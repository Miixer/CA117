import sys

def ranks(s):
    rank = s[-1]
    return int(rank)

def main():
    count = 0
    nothing = 0
    one_pair = 0
    two_pairs = 0
    three_of_a_kind = 0
    straight = 0
    flush = 0
    full_house = 0
    four_of_a_kind = 0
    straight_flush = 0
    royal_flush = 0
    
    for line in sys.stdin:
        count += 1
        line = line.strip()
        num = ranks(line)
        if num == 0:
            nothing += 1
        elif num == 1:
            one_pair += 1
        elif num == 2:
            two_pairs += 1
        elif num == 3:
            three_of_a_kind += 1
        elif num == 4:
            straight += 1
        elif num == 5:
            flush += 1 
        elif num == 6:
            full_house += 1
        elif num == 7:
            four_of_a_kind += 1
        elif num == 8:
            straight_flush += 1
        elif num == 9:
            royal_flush += 1

    count = count/100
    print("The probability of nothing is {:.4f}%".format(nothing/count))
    print("The probability of one pair is {:.4f}%".format(one_pair/count))
    print("The probability of two pairs is {:.4f}%".format(two_pairs/count))
    print("The probability of three of a kind is {:.4f}%".format(three_of_a_kind/count))
    print("The probability of a straight is {:.4f}%".format(straight/count))
    print("The probability of a flush is {:.4f}%".format(flush/count))
    print("The probability of a full house is {:.4f}%".format(full_house/count))
    print("The probability of four of a kind is {:.4f}%".format(four_of_a_kind/count))
    print("The probability of a straight flush is {:.4f}%".format(straight_flush/count))
    print("The probability of a royal flush is {:.4f}%".format(royal_flush/count))

if __name__ == '__main__':
    main()
