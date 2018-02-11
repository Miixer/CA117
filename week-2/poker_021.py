import sys

ranks = {
    "0" : {"nothing": 0,},
    "1" : {"one pair": 0,},
    "2" : {"two pairs": 0,},
    "3" : {"three of a kind": 0,},
    "4" : {"a straight": 0,},
    "5" : {"a flush": 0,},
    "6" : {"a full house": 0,},
    "7" : {"four of a kind": 0,},
    "8" : {"a straight flush": 0,},
    "9" : {"a royal flush": 0,},
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