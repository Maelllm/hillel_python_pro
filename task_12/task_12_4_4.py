# https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python

def alphabet_position(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    text_2 = ""
    for i in text:
        if i.lower() in alphabet:
            text_2 += f'{alphabet.index(i.lower()) + 1} '
    return text_2[:-1]
