from pandas import DataFrame

i = 0
l = []

while i < 5:
    x = input().split()
    li = []
    for value in x:
        li.append(int(value))
    l.append(li)
    i += 1

df = DataFrame(l)
center_row, center_column = 2, 2

for i, row in df.iterrows():
    if sum(row) == 1:
        row_loc = i

for i, column in df.iteritems():
    if sum(column) == 1:
        column_loc = i

delta_y = abs(column_loc - center_column)
delta_x = abs(row_loc - center_row)

minimum_moves = delta_x + delta_y

print(minimum_moves)
