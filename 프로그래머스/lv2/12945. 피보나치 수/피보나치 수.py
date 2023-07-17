def fibo(n):
    cur = 0
    next = 1
    for i in range(n):
        tmp = cur
        cur = next
        next = tmp + next
    return cur

def solution(n):
    answer = 0
    return fibo(n)%1234567