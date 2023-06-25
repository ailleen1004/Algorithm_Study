def solution(n, arr1, arr2):
    answer = []
    map1 = [[0 for _ in range(n)] for _ in range(n)]
    map2 = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        count = 0
        div = arr1[i]
        if div==0:
            continue
        while(1):
            if div==1:
                map1[i][count]=1
                break
            div, mod = divmod(div, 2)
            map1[i][count]=mod
            count += 1
        map1[i].reverse()
    for i in range(n):
        count = 0
        div = arr2[i]
        if div==0:
            continue
        while(1):
            if div==1:
                map2[i][count]=1
                break
            div, mod = divmod(div, 2)
            map2[i][count]=mod
            count += 1
        map2[i].reverse()
    for i in range(n):
        map = ''
        for j in range(n):
            if map1[i][j]==0 and map2[i][j]==0:
                map += " "
            else:
                map += "#"
        answer.append(map)
    return answer