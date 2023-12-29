def search(words, w):
    for i in words:
        if i==w:
            return 1
    return -1

def solution(n, words):

    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0] or search(words[:i], words[i]) == 1:
            return [i%n+1, int(i/n)+1]

    return [0, 0]