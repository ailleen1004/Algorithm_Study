def solution(a, b, n):
    answer = 0
    while(n>=a):
        cola = 0
        while(cola<=n):
            cola += a
        cola -= a
        n -= cola
        n += (cola/a)*b
        answer += (cola/a)*b
    return answer