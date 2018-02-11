import sys

ranks = {
    0 : "nothing",
    1 : "one pair",
    2 : "two pairs",
    3 : "three of a kind",
    4 : "a straight",
    5 : "a flush",
    6 : "a full house",
    7 : "four of a kind",
    8 : "a straight flush",
    9 : "a royal flush",
}


def poker(d, hand):
    rank = hand[-1]
    if rank in d:
        for key in d[rank]:
            d[rank][key] += 1
    return d

def main():
    count = 0
    for line in sys.stdin:
        count += 1
        poker(ranks, line.strip())
    for rank in ranks:
        for key in ranks[rank]:
            p = (ranks[rank][key]/count) * 100
            print("The probability of {} is {:.4f}%".format(key,p))


if __name__ == '__main__':
    main()