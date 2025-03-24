def solution(friends, gifts):
    answer = [0 for _ in range(len(friends))]
    
    give_take = {}
    for i, f in enumerate(friends):
        give_take[f] = [0 for _ in range(len(friends)+1)] # 각 사람에게 준 선물 개수, 선물 지수(준 선물 - 받은 선물)
        give_take[f].append(i) # 인덱스
    
    for g in gifts:
        gift = g.split(' ')
        give_id = gift[0]
        take_id = gift[1]
        take_index = give_take[take_id][-1]
        give_take[give_id][take_index] += 1
        give_take[give_id][-2] += 1
        give_take[take_id][-2] -= 1
        
    # print(give_take)
    ind = 0
    for key, val in give_take.items():
        if key == friends[-1]:
            # print(answer)
            return max(answer)
        for i, v in enumerate(val[ind+1:-2]):
            take_id = friends[i+ind+1]
            
            # 1. 두 사람 사이 더 많은 선물을 준 사람이 선물 +1
            if give_take[key][i+ind+1] > give_take[take_id][ind]: # 전자가 더 많이 줌
                answer[ind] += 1
            elif give_take[key][i+ind+1] < give_take[take_id][ind]: # 후자가 더 많이 줌
                answer[i+ind+1] += 1
            
            # 2. 선물을 주고받은 기록이 없거나 같으면, 선물지수가 큰 사람이 선물 +1
            elif give_take[key][i+ind+1] == give_take[take_id][ind]:            
                # 3. 두 사람의 선물지수도 같다면, 주고받지 X
                if give_take[key][-2] > give_take[take_id][-2]:
                    answer[ind] += 1
                elif give_take[key][-2] < give_take[take_id][-2]:
                    answer[i+ind+1] += 1
        ind += 1
    
    return max(answer)