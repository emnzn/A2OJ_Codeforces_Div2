n = int(input())
v = input().split()
v_int = []
index = 0
my_coins = []

if n >= 0 and n <= 100:
    for x in sorted(v, reverse=True):
        v_int.append(int(x))

    for x in v_int:
        while sum(my_coins) <= sum(v_int[index:len(v_int)]):
            my_coins.append(x)
            index += 1

print(len(my_coins))