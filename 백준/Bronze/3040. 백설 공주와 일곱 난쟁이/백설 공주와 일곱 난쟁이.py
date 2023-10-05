import itertools
import sys
sys.setrecursionlimit(10 ** 6)
num_list = []
for _ in range(9):
    num_list.append(int(sys.stdin.readline()))

comb = list(itertools.combinations(num_list,7))
for c in comb:
    if sum(c) ==100:
        list(c).sort()
        for i in c:
            print(i)