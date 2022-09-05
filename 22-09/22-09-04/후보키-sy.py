'''
https://school.programmers.co.kr/learn/courses/30/lessons/42890
배운 것
1. a.issubset(b) => a가 b의 subset인가?
2. from itertools import combinations -> 조합 사용
3. combinations(a,b) -> a에서 b개의 조합 찾기
4. 리스트 연결 => a.extend(b) 
5. 문자열, 숫자, 튜플만 set에 넣었을 경우 중복제거가 가능!!


'''
from itertools import combinations
answer = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
num = [i for i in range(len(answer[0]))]
tot = []
h = len(answer)
w = len(answer[0])

combi = []
for i in range(1,w+1):
    combi.extend(list(combinations(num,i)))

for i in combi:
    test = [tuple([item[key] for key in i]) for item in answer]
    print(test)
    # 유일키
    if len(set(test)) == len(test):
        #후보키
        bool = True
        for x in tot:
            if set(x).issubset(set(i)):
                bool = False
                break
        if bool:
            tot.append(i)
print(len(tot))
