'''
https://www.acmicpc.net/status?user_id=sophia5460&problem_id=16198&from_mine=1
list.remove(a) -> a원소 지우기
del list[idx] -> idx번호의 원소 지우기
계속 remove로 했어서 틀렸다. 같은 수가 나올수도 있는데 생각을 안함!
'''
import sys
import copy
N = int(input())
list_ = list(map(int,sys.stdin.readline().strip().split()))
max_ = -1

def backtracking(tmp,tot,idx):
    global max_
    org = tot
    if len(tmp) == 2:
        max_ = max(max_,tot)
        return
    if idx >= len(tmp)-1:
        return
    #print(tmp)
    
    #선택 할 경우
    tot += tmp[idx-1]*tmp[idx+1]
    new = copy.deepcopy(tmp)
    del new[idx]
    backtracking(new,tot,1)
    
    #선택 안할 경우
    backtracking(tmp,org,idx+1)
backtracking(list_,0,1)
print(max_)
