def new_format(string):
    i = 0
    string_2 = ""
    while i < len(string):
        if i % 3 == 0 and i != 0:
            string_2 += "."
        string_2 += string[::-1][i]
        i += 1
    return string_2[::-1]


# code here
assert (new_format("1000000") == "1.000.000")
assert (new_format("100") == "100")
assert (new_format("1000") == "1.000")
assert (new_format("100000") == "100.000")
assert (new_format("10000") == "10.000")
assert (new_format("0") == "0")
