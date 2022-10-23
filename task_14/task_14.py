# https://www.codewars.com/kata/514b92a657cdc65150000006

def solution(number):
    if number < 0:
        return 0
    a = range(number)
    b = []
    for i in a:
        if i % 3 == 0:
            b.append(i)
        if i % 5 == 0 and i not in b:
            b.append(i)
    return sum(b)


# https://www.codewars.com/kata/514a024011ea4fb54200004b

def domain_name(url):
    if "www" in url:
        return url[url.index('.') + 1:url[url.index('.') + 1:].index(".") + url.index('.') + 1]
    elif "http" in url:
        return url[url.index('/') + 2:url.index(".")]
    else:
        return url[:url.index(".")]
