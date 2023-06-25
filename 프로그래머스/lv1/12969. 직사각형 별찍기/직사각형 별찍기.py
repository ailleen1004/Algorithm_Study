a, b = map(int, input().strip().split(' '))
star = ''
for i in range(a):
    star += "*"
for i in range(b):
    print(star)