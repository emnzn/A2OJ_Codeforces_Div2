s = input()
index = 0
l = []
new_s = ''

for n in s:
    if n != '+' and n != ' ':
        l.append(n)

for n in sorted(l):
    new_s = new_s + '{}'.format(n)

print('+'.join(new_s))