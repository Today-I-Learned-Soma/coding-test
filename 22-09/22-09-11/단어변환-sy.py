'''
https://school.programmers.co.kr/learn/courses/30/lessons/43163
1. 차이가 나는 단어가 하나인지 체크하는 함수
2. backtracking으로 갔다가 뒤로 돌아가야 할 듯
'''
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
def check(A,B):
    cnt = 0
    for a,b in zip(A,B):
        if a != b:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False
min_ = 1000
def backtracking(begin, target, words, answer):
    global min_
    if begin == target:
        min_ = min(min_, answer)
        return
    for idx, word in enumerate(words):
        if check(begin, word):
            words.remove(word)
            backtracking(word,target,words,answer+1)
            words.append(word)
def solution(begin ,target, words):
    backtracking(begin,target,words,0)
    if  min_ == 1000:
        print(0)
    else:
        print(min_)

solution(begin,target,words)


def solution(begin, target, words):
    answer = 0
    Q = [begin]

    while True:
        temp_Q = []
        for word_1 in Q:
            if word_1 == target:
                    return answer
            # 뒤에서부터 빼는 이우 -> pop하기 위함
            # 다시 사용 할 수 있으니까 
            for i in range(len(words)-1, -1, -1):
                word_2 = words[i]
                # 한단어만 차이가 날 경우
                if sum([x!=y for x, y in zip(word_1, word_2)]) == 1:
                    temp_Q.append(words.pop(i))
            print(temp_Q)

        if not temp_Q:
            return 0
        Q = temp_Q
        answer += 1
solution(begin,target,words)
