# About 40 minutes for solving
hills = [4, 1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 2, 2, 2, 2, 1]

lake = [0, max(hills), 0]
bottom = 0
previous = 0

for i in hills:
    if i < previous:
        if previous > lake[0]:
            lake[0] = previous
            lake[1] = i
            lake[2] = 0
    if i < lake[1]:
        lake[1] = i
    if i > lake[1]:
        if i > lake[2]:
            lake[2] = i
        if min((lake[0] - lake[1]), (lake[2] - lake[1])) > bottom:
            bottom = min((lake[0] - lake[1]), (lake[2] - lake[1]))
    previous = i

print(f'Lake is about {bottom} deep')
