'''
https://school.programmers.co.kr/learn/courses/30/lessons/64062#
내생각 : 슬라이딩 윈도우 문제
k사이즈 별로 움직인 다음 k 내부에서는 max값, 전체적으로는 min값을 구하면 답이 나올 듯

참고 : 이분탐색 기법 이용
'''
import queue
stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]	
k = 3
def solution(stones,k):
    start = [stones[i] for i in range(k)]
    min_ = max(start)
    for i in range(k,len(stones) - k):
        start.pop(0)
        start.append(stones[i])
        min_ = min(min_,max(start))
    print(min_)
solution(stones,k)

def solution(stones,k):
    start = 1
    end = 200000
    answer = -1
    while start <= end:
        jump = (start+end)//2
        # 더 크게 점프를 해야 함
        
        if jump > k:
            end = jump - 1
        else:
            start = jump + 1
            answer = 