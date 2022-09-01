'''
https://www.acmicpc.net/problem/11060 (10분)

'''

import sys
N = int(input())
A = list(map(int,sys.stdin.readline().strip().split()))
inf = 10**10
dp = [inf for _ in range(N)]
dp[0] = 0

for i,a in enumerate(A):
    num = a
    cur_num = A[i]
    if cur_num < 1:
        continue
    for j in range(1,a+1):
        if i+j < N:
            dp[i+j] = min(dp[i+j],dp[i] + 1)
            
dp[N-1] == inf ? print(-1)
if dp[N-1] == inf:
    print(-1)
else:
    print(dp[N-1])