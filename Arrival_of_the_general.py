import numpy as np

n = int(input())
s = input().split()
l = []

for soldier in s:
    l.append(int(soldier))

l = np.array(l)
swaps = 0

shortest = np.where(l == min(l))
tallest = np.where(l == max(l))
tallest_int = tallest[0][0]

if len(shortest[0]) > 1:
    shortest_int = shortest[0][max(shortest[0])]
else:
    shortest_int = shortest[0][0]

if tallest_int != 0:
    swaps = swaps + tallest_int

if shortest_int != len(l) - 1:
    swaps = swaps + ((len(l) - 1) - shortest_int)

if len(l) == 2 or tallest_int > shortest_int:
    print(swaps - 1)

else:
    print(swaps)
