import sys
N,M = map(int,sys.stdin.readline().strip().split())
candy = []
max_ = [[0]*N for _ in range(M)]
X = [0,1,1]
Y = [1,0,1]
for i in range(N):
    tmp = list(map(int,sys.stdin.readline().strip().split()))
    candy.append(tmp)
for i in range(N):
    for j in range(M):
        cur = max_[i][j]
        for _ in range(3):
            dy = i + Y[_]
            dx = j + X[_]
            if 0<=dy<N and 0<=dx<M:
                max_[dy][dx] = max(cur + candy[dy][dx])
print(max_)

