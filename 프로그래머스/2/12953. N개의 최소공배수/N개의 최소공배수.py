import math

def solution(arr):
    
    lcm = arr[0]
    
    for i in range(1, len(arr)):
        # 최대공약수
        gcd = math.gcd(lcm, arr[i])
        # 최소공배수
        lcm = (lcm * arr[i]) // gcd
    
    return lcm