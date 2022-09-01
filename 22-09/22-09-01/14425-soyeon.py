'''
https://www.acmicpc.net/problem/14425
알게된점
- 시간초과가 날 때는 자료형을 바꿔보자!
- list보다 set, dict는 O(1)이기 때문에 훨씬 시간복잡도가 낮다
'''
import sys
N,M = map(int,sys.stdin.readline().strip().split())
S = set(input() for _ in range(N))

cnt = 0
for i in range(M):
    tmp = input()
    if tmp in S:
        cnt += 1
print(cnt)