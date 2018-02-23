import sys

def points(par):
   p = par <= 2 and - par + 2 or 0
   return p

def handi(rank, handicap):
   return int(handicap // 18 + (handicap % 18 >= rank))

def holescore(score, rank, handicap, par):
   point = points(score - handi(rank, handicap) - par)
   return point
 
def main(): 
   pars = [int(n) for n in input().split()]
   index = [int(n) for n in input().split()]
   players = [p.split() for p in sys.stdin] 
   rank = [[], []]
   longest_name = -1
   for p in players:
      name = " ".join(p[:-19])
      handicap = int(p[-19])
      total = 0
      for i, score in enumerate(p[-18:]):
         if score != "X" and score.isdigit():
            total += holescore(int(score), index[i], handicap, pars[i])
         elif not score.isdigit() and score != "X":
            total = "Disqualified"
            break

      rank[total == "Disqualified"].append((name, total))
      longest_name = max(longest_name, len(name))
   ranklist = sorted(rank[0], key=lambda a: a[1], reverse = True) + rank[1]
   for item in ranklist:
      print("{:>{}} : {:2}".format(item[0], longest_name, item[1]))

if __name__ == '__main__':
   main()