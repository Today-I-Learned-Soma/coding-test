'''
https://www.acmicpc.net/problem/2800
괄호를 빼버리는 부분에 대한 고민 중 그냥 빈칸으로 두었다가 나중에 합치면 어떨까라는 생각을 했다.
억지 같았는데 다른 사람들도 그렇게 풀었군~
'''
import sys
import itertools
galho = sys.stdin.readline().strip()

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
    tmp = list(galho)
    for x,y in way:
        tmp[x] = ""
        tmp[y] = ""
    answer.add(''.join(str(s) for s in tmp))
answer = list(answer)
answer.sort()
for an in answer:
    print(an)
