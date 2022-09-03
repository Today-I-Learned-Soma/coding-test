import sys
N,T = map(int,sys.stdin.readline().strip().split())
scores = []
answer = [[0]*10001 for _ in range(101)]
for _ in range(N):
    scores.append(list(map(int,sys.stdin.readline().strip().split())))
#print(scores)
for i in range(N):
    time = scores[i][0]
    score = scores[i][1]
    for j in range(time):
        answer[i][j] = answer[i-1][j]
    for j in range(time,T+1):
        answer[i][j] = max(answer[i-1][j], answer[i-1][j-time] + score)
print(answer[N-1][T])