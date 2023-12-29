def solution(brown, yellow):

    y = int(brown/2) - 2
    for i in range(1, y):
        if yellow == (y-i)*i:
            return [y-i+2, i+2]
