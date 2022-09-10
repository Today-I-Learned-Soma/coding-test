import sys
k = int(input())
n = int(input())
origin = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
now = origin[:k]
row = list(sys.stdin.readline().strip())
sadari = []
answer = -1
for i in range(n):
    tmp = list(sys.stdin.readline().strip())
    if tmp[0] == '?':
        answer = i
    sadari.append(tmp)

for idx, r in enumerate(row):
    #idx = 현재위치
    tmp = -1
    org_idx = -1
    for row_idx, j in enumerate(now):
        if j == r:
            org_idx = row_idx
            break
    for i in range(n):
        # 이동
        if i == answer:
            tmp = idx
        if idx == 0 and sadari[i][idx] == '-':
            idx += 1
        elif idx == k-1 and sadari[i][idx-1] == '-' :
            idx -= 1
        elif idx > 0 and sadari[i][idx-1] == '-' :
            idx -= 1
        elif idx < k -1 and sadari[i][idx] == '-' :
            idx += 1
    # 틀릴 때
    if r != row[idx]:
        # 더 큰경우
        if org_idx < idx:
            sadari[answer][tmp-1] = '-'
        else:
            sadari[answer][tmp] = '-'
print(sadari[answer])
        
        