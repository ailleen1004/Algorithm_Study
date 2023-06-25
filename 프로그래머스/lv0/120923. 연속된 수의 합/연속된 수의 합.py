def solution(num, total):
    answer = []
    result = total
    count = 0
    while(result>=total):
        result = 0
        for i in range(num):
            answer.append(total+num-i-count)
            result += total+num-i-count
        if result == total:
            answer = sorted(answer)
            break
        else:
            answer = []
            count += 1
            continue
    return answer