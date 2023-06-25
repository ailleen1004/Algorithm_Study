def solution(babbling):
    answer = 0
    for i in babbling:
        a = i.replace("aya", "1")
        if "11" in a:
            continue
        b = a.replace("ye", "2")
        if "22" in b:
            continue
        c = b.replace("woo", "3")
        if "33" in c:
            continue
        d = c.replace("ma", "4")
        if "44" in d:
            continue
        if d.isdigit()  is True:
            answer+=1
    return answer