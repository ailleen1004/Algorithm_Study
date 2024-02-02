import collections

def solution(want, number, discount):
    answer = 0
    l = []
    
    want_num = {key: value for key, value in zip(want,number)} # 원하는 것 dict로 저장
    want_num = sorted(want_num.items())
    
    for i in range(len(discount)-sum(number)+1):
        d = dict(collections.Counter(discount[i:i+sum(number)])) # 요소 count해 dict로 저장
        l.append(sorted(d.items()))
    
    for i in l:
        if want_num == i:
            answer+=1
    
    return answer