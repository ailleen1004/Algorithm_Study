def solution(s):
    answer = True
    count = [0, 0]
    arr = list(s)
    for i in arr:
        if i=="p" or i=="P":
            count[0]+=1
        elif i=="y" or i=="Y":
            count[1]+=1
    if count[0]==count[1]:
        return True
    else:
        return False