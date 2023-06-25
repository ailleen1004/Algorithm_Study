def solution(s):
    answer = True
    if s.isdigit()==False or (len(s)!=4 and len(s)!=6):
        answer = False
    return answer