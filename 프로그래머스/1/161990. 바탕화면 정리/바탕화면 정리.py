def solution(wallpaper):
    answer = []
    
    # 좌상단 꼭짓점 저장
    papers = []
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j]=='#':
                papers.append([i, j])
    
    answer = [papers[0][0], papers[0][1], papers[-1][0]+1, papers[0][1]+1]
    
    for p in papers[1:]:
        if answer[1] > p[1]:
            answer[1] = p[1]
        elif answer[3] < p[1]+1:
            answer[3] = p[1]+1
            
    return answer