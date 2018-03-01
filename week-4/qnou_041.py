import sys

def main():
    words = [w.strip() for w in sys.stdin]
    qnou = [word.strip() for word in words if word.strip().lower().count("q") > word.strip().lower().count("qu")]
    print("Words with q but no u: {}".format(qnou))

if __name__ == '__main__':
    main()