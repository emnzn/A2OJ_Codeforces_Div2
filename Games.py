import numpy as np

n = int(input())
count = 0

i = n
a_l = []
while i > 0:
    l = []
    team = input().split()
    for j in team:
        l.append(int(j))
    a_l.append(l)
    i -= 1

for t in a_l:
    r = len(a_l) - 1
    i = 0
    while r >= 0:
        if t[0] == a_l[r][1]:
            count = count + 1
        r -= 1

print(count)
