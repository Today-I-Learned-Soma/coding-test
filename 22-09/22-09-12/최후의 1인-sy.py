import sys
import copy
def divide(y,x,new_game):
    list_ = []
    for i in range(y,y+2):
        for j in range(x,x+2):
            list_.append(new_game[i][j])
    list_.sort()
    return list_[-2]

def conquer(n,game):
    new_game = [[] for _ in range(int(n/2))]
    for i in range(0,n,2):
        for j in range(0,n,2):
            new_game[int(i/2)].append(divide(i,j,game))
    return new_game

N = int(input())
game = []
for i in range(N):
    game.append(list(map(int,sys.stdin.readline().strip().split())))

while N != 1:
    new_game = conquer(N,game)
    game = copy.deepcopy(new_game)
    N = int(N/2)
print(game[0][0])

