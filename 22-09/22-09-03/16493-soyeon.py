'''
https://www.acmicpc.net/problem/16493
오랜만에 배낭문제를 풀다보니 아 먼가 이차원 배열에서 뭘 뺀다음에 value를 더하는 거였는데~ 하면서 긴가민가했다
처음으로 혼자서 풀어본거라 머리에 잘 각인된듯!
인덱스에 맞게 배열 크기 잘 설정하기

'''
import sys
N,M = map(int,sys.stdin.readline().strip().split())
book = []
answer = [[0]*(N+1) for _ in range(M+1)]
for _ in range(M):
    book.append(list(map(int,sys.stdin.readline().strip().split())))
for i in range(M):
    day = book[i][0]
    value = book[i][1]
    #print(day,value)
    for j in range(N+1):
        answer[i][j] = answer[i-1][j]
        if j >= day:
           answer[i][j] = max(answer[i][j], answer[i-1][j-day] + value) 
    #print(answer)
print(answer[M-1][N])