import sys
K = int(input())
x,y = map(int,sys.stdin.readline().strip().split())
direction = [[[0,1],[0,0],[1,0]],[[0,0],[0,-1],[1,0]],[[0,0],[0,1],[-1,0]],[[0,0],[0,-1],[-1,0]]]

visited = [[0]*2**K for _ in range(2**K)]
visited[x-1][y-1] = -1
print(visited)

def divided(visited, i, j, n):
    
