# https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python

def is_pangram(s):
    check = "the quick, brown fox jumps over the lazy dog"
    for i in check:
        if ord(i) in range(97, 123):
            if i.lower() not in s.lower():
                return False
    return True
