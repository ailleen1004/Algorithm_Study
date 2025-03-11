def solution(X, Y):
    answer = ''
    
    x_list = {}
    y_list = {}
    same = {}
    
    for i in list(X):
        if i not in x_list:
            x_list[i] = 1
        else:
            x_list[i] += 1
    for i in list(Y):
        if i not in y_list:
            y_list[i] = 1
        else:
            y_list[i] += 1
    
    for x in x_list:
        if x in y_list:
            same[x] = min(x_list[x], y_list[x])
    
    if same == {}:
        return '-1'
    elif len(same) == 1 and '0' in same:
        return '0'
    else:
        while(same != {}):
            m = max(same)
            answer += m
            if same[m] == 1:
                same.pop(m)
            else:
                same[m] -= 1
    return answer