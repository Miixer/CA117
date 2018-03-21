import sys

def result(line):
    mark = 0
    line = line.strip().split(":")
    name, results = line[0], line[1]
    results = results.split(",")
    for result in results:
        try:
            mark += int(result)
        except:
            return (name, 0)

    return name, mark

def main():
    d = {}
    for line in sys.stdin:
        name, mark = result(line)
        d[name] = mark

    exclude = []
    for k,v in sorted(d.items(), key=lambda x: x[1], reverse=True):
        if v > 0:
            print("{} : {}".format(k,v))
        else:
            exclude.append(k)
    
    print("Skipped:")
    for s in exclude:
        print(s)



if __name__ == '__main__':
    main()