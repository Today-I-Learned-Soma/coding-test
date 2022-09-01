'''
https://www.acmicpc.net/problem/6236
이분탐색

'''
import sys
N,M = map(int,sys.stdin.readline().strip().split())
money = []
for i in range(N):
    money.append(int(input()))

min_ = max(money)
max_ = sum(money)

cnt = 0
tmp_cnt = 0
answer = 0

while min_ <= max_:
    tmp_cnt = 1
    mid = (min_+max_) // 2
    tmp = mid
    #print(mid)
    for i in money:
        if i <= tmp:
            tmp -= i
        else:
            tmp_cnt += 1
            tmp = mid - i
        #print(tmp,tmp_cnt)
    if tmp_cnt > M:
        min_ = mid + 1
    else:
        max_ = mid - 1
        answer = mid

print(answer)
