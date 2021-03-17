n = input()
lucky_n = []

if int(n) > 0 and int(n) < 1001:
    if int(n) % 4 == 0 or int(n) % 7 == 0:
        for x in n:
            lucky_n.append(x)
    else:
        for x in n:
            if int(x) == 4 or int(x) == 7:
                lucky_n.append(x)

    if len(lucky_n) != len(n):
        print('NO')

    else:
        print('YES')
