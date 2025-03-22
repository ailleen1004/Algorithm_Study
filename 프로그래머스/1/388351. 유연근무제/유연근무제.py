def solution(schedules, timelogs, startday):
    answer = 0
    
    check = [0 for _ in range(len(schedules))]
    if startday < 6:
        for i, time in enumerate(timelogs):
            starttofri = time[:6-startday] # startday ~ FRIDAY
            montostart = time[8-startday:] # MONDAY ~ startday-1
            maxtime = schedules[i]+10
            if maxtime%100 >= 60:
                maxtime += 100
                maxtime -= 60
                
            for s in starttofri:
                if s<=maxtime:
                    check[i] += 1
                else:
                    break
            for s in montostart:
                if s<=maxtime:
                    check[i] += 1
                else:
                    break
    
    else:
        for i, time in enumerate(timelogs):
            montofri = time[8-startday:13-startday] # MONDAY ~ FRIDAY
            maxtime = schedules[i]+10
            if maxtime%100 >= 60:
                maxtime += 100
                maxtime -= 60
            for s in montofri:
                if s<=maxtime:
                    check[i] += 1
                else:
                    break
                    
    for c in check:
        if c==5:
            answer += 1
    return answer