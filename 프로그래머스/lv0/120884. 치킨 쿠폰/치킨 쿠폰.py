def solution(chicken):
    coupon = 0
    service = 0
    for i in range(1, chicken+1):
        coupon += 1
        if coupon % 10 == 0:
            service += 1
            coupon += 1
    return service