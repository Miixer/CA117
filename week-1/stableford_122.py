import sys

#points = lambda par: par <= 2 and -par + 2 or 0
#hole_score = lambda score, rank, handicap, par: points(score - ((handicap // 18) + int(handicap % 18 >= rank)) - par)

def points(par):
   return par <= 2 and -par + 2 or 0

def hole_score(score, rank, handicap, par):
   return points(score - ((handicap // 18) + int(handicap % 18 >= rank)) - par)
 
def main(): 
   pars = [int(n) for n in input().split()]
   index = [int(n) for n in input().split()]
   players = [p.split() for p in sys.stdin] 
   ranked = [[], []]
   longest_name = -1
   for p in players:
      name = " ".join(p[:-19])
      handicap = int(p[-19])
      total = 0
      for i, score in enumerate(p[-18:]):
         if score != "X" and score.isdigit():
            total += hole_score(int(score), index[i], handicap, pars[i])
         elif not score.isdigit() and score != "X":
            total = "Disqualified"
            break
      ranked[total == "Disqualified"].append((name, total))
      longest_name = max(longest_name, len(name))
   ranked_list = sorted(ranked[0], key=lambda a: a[1], reverse = True) + ranked[1]
   for item in ranked_list:
      print("{:>{}} : {:2}".format(item[0], longest_name, item[1]))

if __name__ == '__main__':
   main()