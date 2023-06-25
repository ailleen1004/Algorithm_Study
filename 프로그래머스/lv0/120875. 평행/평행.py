def solution(dots):
    answer = 0
    if dots[1][0]-dots[0][0]!=0 and dots[3][0]-dots[2][0]!=0:
        if (dots[1][1]-dots[0][1])/(dots[1][0]-dots[0][0])==(dots[3][1]-dots[2][1])/(dots[3][0]-dots[2][0]):
            answer = 1
    elif dots[1][1]-dots[0][1]!=0 and dots[3][1]-dots[2][1]!=0:
        if (dots[1][0]-dots[0][0])/(dots[1][1]-dots[0][1])==(dots[3][0]-dots[2][0])/(dots[3][1]-dots[2][1]):
            answer = 1
        
    if dots[2][0]-dots[0][0]!=0 and dots[3][0]-dots[1][0]!=0:
        if (dots[2][1]-dots[0][1])/(dots[2][0]-dots[0][0])==(dots[3][1]-dots[1][1])/(dots[3][0]-dots[1][0]):
            answer = 1
    elif dots[2][1]-dots[0][1]!=0 and dots[3][1]-dots[1][1]!=0:
        if (dots[2][0]-dots[0][0])/(dots[2][1]-dots[0][1])==(dots[3][0]-dots[1][0])/(dots[3][1]-dots[1][1]):
            answer = 1
        
    if dots[3][0]-dots[0][0]!=0 and dots[2][0]-dots[1][0]!=0:
        if (dots[3][1]-dots[0][1])/(dots[3][0]-dots[0][0])==(dots[2][1]-dots[1][1])/(dots[2][0]-dots[1][0]):
            answer = 1
    elif dots[3][1]-dots[0][1]!=0 and dots[2][1]-dots[1][1]!=0:
        if (dots[3][0]-dots[0][0])/(dots[3][1]-dots[0][1])==(dots[2][0]-dots[1][0])/(dots[2][1]-dots[1][1]):
            answer = 1
    return answer