def solution(ingredient):
    answer = 0
    
    hamburger = []
    
    for i in ingredient:
        if i == 1: # 빵
            if len(hamburger) == 0:
                hamburger.append([i])

            elif hamburger[-1] == [1, 2, 3]: # 마지막
                answer += 1
                hamburger.pop(-1)

            else: # 처음
                hamburger.append([i])

        elif len(hamburger) != 0 and i == 2: # 야채
            if hamburger[-1] == [1]: 
                hamburger[-1].append(i)
            
            else:
                hamburger.append([i])
            

        elif len(hamburger) != 0 and i == 3: # 고기
            if hamburger[-1] == [1, 2]:
                hamburger[-1].append(i)  
            
            else:
                hamburger.append([i])
        
    return answer