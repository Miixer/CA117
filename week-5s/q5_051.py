import sys

def times(string):
	m, s = string.split(":")
	return int(m)

def main():
	d = {}
	for line in sys.stdin:
		try:
			info = line.strip().split()
			d[info[0]] = min(info[1:], key=times)
		except ValueError:
			continue

	winner = min(d.items(), key=lambda x: times(x[1]))
	print("{} : {}".format(winner[0], winner[1]))

if __name__ == '__main__':
	main()