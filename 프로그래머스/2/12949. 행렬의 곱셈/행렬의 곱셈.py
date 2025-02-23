def solution(arr1, arr2):
    answer = [[] for i in range(len(arr1))]
    new_arr2 = [[] for j in range(len(arr2[0]))]
    
    
    for arr in arr2:
        i = 0
        for narr in new_arr2:
            narr.append(arr[i])
            i+=1
    
    for num1, a1 in enumerate(arr1):
        for num2, a2 in enumerate(new_arr2):
            result = 0
            for i in range(len(a1)):
                result += a1[i]*a2[i]
            answer[num1].append(result)
    
    return answer