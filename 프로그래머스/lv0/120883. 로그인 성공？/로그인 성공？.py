def solution(id_pw, db):
    answer = ''
    for i in range(len(db)):
        if db[i][0]==id_pw[0] and db[i][1]==id_pw[1]:
            answer = "login"
            break
        elif db[i][0]==id_pw[0] and db[i][1]!=id_pw[1]:
            answer = "wrong pw"
            break
        else:
            answer = "fail"    
    return answer