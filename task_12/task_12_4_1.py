# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python
def filter_list(l):
    new_list = []
    for i in l:
        try:
            if i >= 0:
                new_list.append(i)
        except:
            pass
    return new_list
