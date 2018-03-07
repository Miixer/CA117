import sys

def dic(names, times):
	d = {}
	d[names] = times
	return d

def main():
	d = {}
	nam = []
	tim = []
	info = [line.strip() for line in sys.stdin]
	for n in info:
		names, times = n.split()[0], n.split()[1:]
		nam.append(names)
		try:
			times = min(sorted(times))
			tim.append(times)
		except:
			continue
		times = times.replace(":", "")
		d[names] = times
	x = sorted((d.values()))
	for k,v in d.items():
		print(k)
	#fastestime = print(min(x, key=int))
	



if __name__ == '__main__':
	main()