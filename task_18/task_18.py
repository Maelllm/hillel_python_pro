def sum_of_intervals(a):
    temo_list = dict()
    for i in a:
        if i[0] not in temo_list.keys():
            temo_list[i[0]] = i[1]
        else:
            if i[1] > temo_list[i[0]]:
                temo_list[i[0]] = i[1]

    temo_list = list(sorted(temo_list.items()))

    min = temo_list[0][0]
    max = temo_list[0][1]
    list_1 = [temo_list[0][0], temo_list[0][1]]

    length = 0

    for i in temo_list:
        length += (list_1[1] - list_1[0])
        i = [i[0], i[1]]
        if i[0] <= max and i[0] >= min:
            i[0] = max
        if i[1] <= max:
            i[1] = max
        list_1 = [i[0], i[1]]
        max = i[1]

    length += (list_1[1] - list_1[0])

    return length
