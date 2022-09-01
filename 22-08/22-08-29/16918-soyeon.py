'''
https://www.acmicpc.net/problem/16918
배열끼리의 복사는 deepcopy를 해야한다는 사실을 알게됨
idx랑 초가 안맞을 때는 억지로 끼워맞추기
'''
import sys
import copy
R,C,N = map(int,sys.stdin.readline().strip().split())
miro = []
bomb = set()
all_ = set()

for _ in range(R):
    tmp = list(sys.stdin.readline().strip())
    for i,j in enumerate(tmp):
        if j != '.':
            bomb.add((_,i))
        all_.add((_,i))
    miro.append(tmp)

if N % 2 == 0:
    for i in range(R):
        for j in range(C):
            print('O',end='')
        print()
    exit()


X = [-1,0,0,1]
Y = [0,1,-1,0]

def in_range(i,j):
    if 0<=i<R and 0<=j<C:
        return True
    return False

new_bomb = copy.deepcopy(bomb)
def bfs():
    tmp = copy.deepcopy(new_bomb)
    for y,x in tmp:
        for _ in range(4):
            dy = Y[_] + y
            dx = X[_] + x
            if in_range(dy,dx):
                new_bomb.add((dy,dx))

def pr():
    for i in range(R):
        for j in range(C):
            if (i,j) in new_bomb:
                print('O',end='')
            else:
                print('.',end='')
        print()

for i in range(1,N):
    if i % 2 == 1:
        bfs()
        bomb = copy.deepcopy(new_bomb)
    if i % 2 == 0:
        new_bomb = all_.difference(bomb)
pr()