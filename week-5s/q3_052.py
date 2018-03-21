def build_dictionary(filename):
   d = {}
   with open(filename, "r") as f:
      for line in f:
         line = line.strip().split()
         d[line[0]] = line[1]
   return d

def extract_range(d, low, high):
   new = {}
   for k,v in d.items():
      if low <= int(v) <= high:
         new[k] = v
   return new