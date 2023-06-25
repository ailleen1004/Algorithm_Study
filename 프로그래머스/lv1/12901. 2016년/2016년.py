def solution(a, b):
    answer = ''
    today = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    month = 1
    day = 1
    count = 0
    while(1):
        if month==a and day==b:
            answer = today[count%7]
            break
        count +=1
        day +=1
        if month==2 and day==29:
            month+=1
            day=0
        elif month<=7:
            if (month%2==1 and day==31) or (month%2==0 and day==30):
                month+=1
                day=0
        elif month>7:
            if (month%2==0 and day==31) or (month%2==1 and day==30):
                month+=1
                day=0
    return answer