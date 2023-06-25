def solution(lottos, win_nums):
    count = 0
    zero = lottos.count(0)
    for i in lottos:
        if i in win_nums:
            count+=1
    answer = [(6 if (count+zero) <= 1 else 7-count-zero), (6 if count <= 1 else 7-count)]
    return answer