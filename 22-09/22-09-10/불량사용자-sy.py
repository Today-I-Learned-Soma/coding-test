'''
https://school.programmers.co.kr/learn/courses/30/lessons/64064

중복순열 : product
from itertools import product
리스트 중 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우의 수를 계산. 원소를 중복하여 뽑는다.
ex)
items = [['a', 'b', 'c,'], ['1', '2', '3', '4'], ['!', '@', '#']]
list(product(*items))
# [('a', '1', '!'), ('a', '1', '@'), ('a', '1', '#'), ('a', '2', '!'), ('a', '2', '@'), ('a', '2', '#'), ('a', '3', '!'), ('a', '3', '@'), ('a', '3', '#'), ('a', '4', '!'), ('a', '4', '@'), ('a', '4', '#'), ('b', '1', '!'), ('b', '1', '@'), ('b', '1', '#'), ('b', '2', '!'), ('b', '2', '@'), ('b', '2', '#'), ('b', '3', '!'), ('b', '3', '@'), ('b', '3', '#'), ('b', '4', '!'), ('b', '4', '@'), ('b', '4', '#'), ('c,', '1', '!'), ('c,', '1', '@'), ('c,', '1', '#'), ('c,', '2', '!'), ('c,', '2', '@'), ('c,', '2', '#'), ('c,', '3', '!'), ('c,', '3', '@'), ('c,', '3', '#'), ('c,', '4', '!'), ('c,', '4', '@'), ('c,', '4', '#')]

'''
#원코드
import copy
user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
list_ = [[]for _ in range(len(banned_id))]
answer = 0
for b_idx, ban in enumerate(banned_id):
    for u_idx, user in enumerate(user_id):
        if len(ban) != len(user):
            continue
        flag = True
        for b, u in zip(ban, user) :
            if b == '*':
                continue
            elif b != u:
                flag = False
                break


        if flag == True:
            list_[b_idx].append(u_idx)
print(list_)
answer_list = set()

def combination(tmp,y):
    global answer_list
    if y == len(banned_id):
        new_tmp = list(copy.deepcopy(tmp))
        new_tmp.sort()
        tuple_tmp = tuple(new_tmp)
        answer_list.add(tuple_tmp)
        print(tuple_tmp)
        return
    for idx, element in enumerate(list_[y]):
        if element not in tmp:
            tmp.add(element)
            combination(tmp,y+1)
            tmp.remove(element)
           

combination(set(),0)
print(len(answer_list))


    

#product 반영 코드
import copy
from itertools import product
user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
list_ = [[]for _ in range(len(banned_id))]
answer = 0
for b_idx, ban in enumerate(banned_id):
    for u_idx, user in enumerate(user_id):
        if len(ban) != len(user):
            continue
        flag = True
        for b, u in zip(ban, user) :
            if b == '*':
                continue
            elif b != u:
                flag = False
                break


        if flag == True:
            list_[b_idx].append(u_idx)
product_ = list(product(*list_))
answer = set()
for pro in product_:
    if len(pro) == len(set(pro)):
        print(sorted(set(pro)))
        answer.add("".join(str(sorted(set(pro)))))
print(len(answer))
