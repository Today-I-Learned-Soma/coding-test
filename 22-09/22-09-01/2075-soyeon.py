'''
https://www.acmicpc.net/problem/2075
알게된점 : 
- heapq -> 가장 작은 원소는 언제나 [0]에 위치함!!
- 5개를 미리 넣어두고 그 다음부터는 가장 작은 원소랑 비교해서 더 크면 집어넣는 방식으로 사용!
'''
import sys
import heapq as h
N = int(input())
queue = []
for _ in range(N):
    tmp = list(map(int,sys.stdin.readline().strip().split()))
    if not queue:
        for j in tmp:
            h.heappush(queue,j)
    else:
        for j in tmp:
            if queue[0] < j:
                h.heappop(queue)
                h.heappush(queue,j)
print(queue[0])



