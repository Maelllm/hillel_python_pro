# https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python

def maskify(cc):
    cc_2 = ""
    i = 0
    while i < len(cc):
        if i <= 3:
            cc_2 += cc[::-1][i]
        elif i > 3:
            cc_2 += "#"
        i += 1
    return cc_2[::-1]
