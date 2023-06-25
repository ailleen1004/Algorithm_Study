def solution(n):
    reverse = ''
    while n > 0: #10진수 -> 3진수, reverse
        n, mod = divmod(n, 3)
        reverse += str(mod)
    return int(reverse, 3)