def solution(park, routes):
    answer = []
    
    i1 = 0
    for p in park:
        if 'S' in p:
            i2 = p.index('S')
            answer = [i1, i2]
            break
        i1 += 1
    
    for r in routes:
        isX = 0
        r = r.split(' ')
        
        # 오른쪽
        if r[0] == 'E':
            for i in range(int(r[1])):
                # 벽을 넘음 or 장애물 있음
                if answer[1] + int(r[1]) >= len(park[answer[0]]) or park[answer[0]][answer[1]+i+1] == 'X':
                    break
                else:
                    isX += 1

            if isX == int(r[1]):
                answer[1] += int(r[1])
        
        # 아래쪽
        elif r[0] == 'S':
            for i in range(int(r[1])):
                # 벽을 넘음 or 장애물 있음
                if answer[0] + int(r[1]) >= len(park) or park[answer[0]+i+1][answer[1]] == 'X':
                    break
                else:
                    isX += 1

            if isX == int(r[1]):
                answer[0] += int(r[1])
        
        # 왼쪽
        elif r[0] == 'W':
            for i in range(int(r[1])):
                # 벽을 넘음 or 장애물 있음
                if answer[1] - int(r[1]) < 0 or park[answer[0]][answer[1]-i-1] == 'X':
                    break
                else:
                    isX += 1

            if isX == int(r[1]):
                answer[1] -= int(r[1])
        
        # 위쪽
        elif r[0] == 'N':
            for i in range(int(r[1])):
                # 벽을 넘음 or 장애물 있음
                if answer[0] - int(r[1]) < 0 or park[answer[0]-i-1][answer[1]] == 'X':
                    break
                else:
                    isX += 1

            if isX == int(r[1]):
                answer[0] -= int(r[1])
                
    return answer