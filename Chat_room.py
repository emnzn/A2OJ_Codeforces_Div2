s = input()
l = []
ref = ['h', 'e', 'l', 'l', 'o']

for x in s:
    if l.count('h') < 1 and x == 'h':
        l.append(x.lower())

    if l.count('e') < 1 and x == 'e':
        l.append(x.lower())

    if l.count('l') < 2 and x == 'l':
        l.append(x.lower())

    if l.count('o') < 1 and x == 'o':
        l.append(x.lower())

if l == ref:
    print('YES')

else:
    print('NO')
