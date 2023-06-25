def solution(dots):
    answer = 1
    x = dots[0][0]
    y = dots[0][1]
    for i in range(1,3):
        if x != dots[i][0]:
            print(dots[i][0])
            answer *= abs(dots[i][0] - x)
            break
    for j in range(1,3):
        if y != dots[j][1]:
            print(dots[j][0])
            answer *= abs(dots[j][1] - y)
            break
    return answer