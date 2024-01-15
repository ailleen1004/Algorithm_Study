# def fibo(n):
#     if n==1:
#         return 1
    
#     elif n==2:
#         return 2    
    
#     return fibo(n-1)+fibo(n-2)

# def solution(n):
    
#     return fibo(n)%1234567

def fibo(n):
    if n==1:
        return 1
    
    elif n==2:
        return 2    
    
    return fibo(n-1)+fibo(n-2)

def solution(n):
    if n==1:
        return 1
    if n==2:
        return 2
    
    fibo = [1, 2]
    for i in range(n-2):
        fibo.append(fibo[-1]+fibo[-2])
    return fibo[-1]%1234567