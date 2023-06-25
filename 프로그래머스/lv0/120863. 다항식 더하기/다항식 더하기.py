def solution(polynomial):
    answer = ''
    x = 0
    y = 0
    arr = polynomial.split(" + ")
    for i in arr:
        if i.strip()[-1] == "x":
            if len(i) == 1:
                x = x + 1
            else:
                x = x + int(i[:-1])
        else:
            y = y + int(i)
    if x != 0 and y != 0:
        if x==1:
            answer = answer + "x + " + str(y)
        else:
            answer = answer + str(x) + "x + " + str(y)
    elif x != 0 and y == 0:
        if x==1:
            answer = answer + "x"
        else:
            answer = answer + str(x) + "x"
    elif x == 0 and y != 0:
        answer = answer + str(y)
    else:
        answer = answer + "0"
    return answer