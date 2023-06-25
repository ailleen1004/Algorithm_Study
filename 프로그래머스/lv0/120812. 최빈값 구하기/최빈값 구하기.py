from collections import Counter

def solution(array):
    answer = 0
    counter = Counter(array) # Counter({3:3, 1:1, 2:1, 4:1})
    most = counter.most_common() #[(3, 3), (1, 1), (2, 1), (4, 1)]
    maximum = most[0][1]
    li = []
    for num in most:
        if num[1]==maximum: # index 1에 들어있는 값이 빈도수
            li.append(num[0]) # li = [(3, 3)]
    if len(li)>=2: # 최빈값이 2개 이상일 때
        answer = -1
    else:
        answer = li[0] # 최빈값이 1개일 때
    return answer