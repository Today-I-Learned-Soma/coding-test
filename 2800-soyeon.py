import itertools
import sys
from itertools import combinations
import copy
galho = list(sys.stdin.readline().strip())

idx = []
pair = []
for i,gal in enumerate(galho):
    if gal == '(':
        idx.append(i)
    elif gal == ')':
        n = idx.pop()
        pair.append([i,n])

ways = []
for i in range(1,len(pair)+1):
    ways.extend(list(itertools.combinations(pair,i)))
answer = set()
for way in ways:
    tmp = copy.deepcopy(galho)
    for x,y in way:
        tmp[x] = ""
        tmp[y] = ""
    answer.add(''.join(str(s) for s in tmp))
answer = list(answer)
answer.sort()
for an in answer:
    print(an)
