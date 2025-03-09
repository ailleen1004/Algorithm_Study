def solution(keymap, targets):
    answer = []
    
    dic = {}
    
    for key in keymap:
        for k in key:
            if k not in dic:
                cnt = key.index(k)+1
                dic[k] = cnt
            elif k in dic and dic[k] > key.index(k)+1:
                dic[k] = key.index(k)+1
                
    # print(dic) -> {'A': 1, 'B': 1, 'C': 2, 'D': 5, 'E': 3, 'F': 4}
    
    for tar in targets:
        a = 0
        for t in tar:
            if t not in dic:
                a = -1
                break
            a += dic[t]
        answer.append(a)
    
    return answer