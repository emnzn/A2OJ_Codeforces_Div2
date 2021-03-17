n = int(input())
Pi = input().split()
index = 0
Pi_int = []
out = list(range(n))
for p in Pi:
    Pi_int.append(int(p))

Pi_sorted = sorted(Pi_int)

for p in Pi_sorted:
    out[Pi_int[index] - 1] = p
    index += 1

print(out)
