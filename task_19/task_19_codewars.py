# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39

def zero(*arg):
    if arg:
        return eval(f'0{arg[0]}')
    return 0


def one(*arg):
    if arg:
        return eval(f'1{arg[0]}')
    return 1


def two(*arg):
    if arg:
        return eval(f'2{arg[0]}')
    return 2


def three(*arg):
    if arg:
        return eval(f'3{arg[0]}')
    return 3


def four(*arg):
    if arg:
        return eval(f'4{arg[0]}')
    return 4


def five(*arg):
    if arg:
        return eval(f'5{arg[0]}')
    return 5


def six(*arg):
    if arg:
        return eval(f'6{arg[0]}')
    return 6


def seven(*arg):
    if arg:
        return eval(f'7{arg[0]}')
    return 7


def eight(*arg):
    if arg:
        return eval(f'8{arg[0]}')
    return 8


def nine(*arg):
    if arg:
        return eval(f'9{arg[0]}')
    return 9


def plus(arg):
    return '+' + str(arg)


def minus(arg):
    return '-' + str(arg)


def times(arg):
    return '*' + str(arg)


def divided_by(arg):
    return '//' + str(arg)


# https://www.codewars.com/kata/5264d2b162488dc400000001

def spin_words(sentence):
    sentence += ' '
    list = []
    a = ''
    b = ''
    for i in sentence:
        if i == " ":
            list.append(a)
            a = ""
        else:
            a += i
    for y in list:
        if len(y) >= 5:
            b += y[::-1]
        else:
            b += y
        b += " "
    return b[:-1]


# https://www.codewars.com/kata/515bb423de843ea99400000a


class PaginationHelper:

    # The constructor takes in an array of items and a integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
        self.amount = len(self.collection)
        self.pages = self.amount // self.items_per_page + 1

    # returns the number of items within the entire collection
    def item_count(self):
        return self.amount

    # returns the number of pages
    def page_count(self):
        return self.pages

    # returns the number of items on the current page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        if page_index < self.pages:
            if page_index == self.pages - 1:
                return self.amount % self.items_per_page
            return self.items_per_page
        return -1

    # determines what page an item is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if item_index >= 0:
            if item_index < self.amount:
                return item_index // self.items_per_page
        return -1


# https://www.codewars.com/kata/51b66044bce5799a7f000003/python
class RomanNumerals:

    @staticmethod
    def to_roman(val):
        amount_1 = (val // 1000) * "M"
        amount_2 = "CM" if val % 1000 // 900 == 1 else ""
        amount_3 = "D" if val % 1000 // 500 == 1 and val % 1000 // 900 == 0 else ""
        amount_4 = "CD" if val % 500 // 400 == 1 and val % 1000 // 900 == 0 else ""
        amount_5 = "" if val % 500 // 400 == 1 else (val % 500 // 100) * "C"
        amount_6 = "XC" if val % 100 // 90 == 1 else ""
        amount_7 = "L" if val % 100 // 90 == 0 and val % 100 // 50 == 1 else ""
        amount_8 = "XL" if val % 50 // 40 == 1 and val % 100 // 90 == 0 else ""
        amount_9 = "" if val % 50 // 40 == 1 else (val % 50 // 10) * "X"
        amount_10 = "IX" if val % 10 == 9 else ""
        amount_11 = "V" if val % 10 // 5 == 1 and val % 10 // 9 == 0 else ""
        amount_12 = "IV" if val % 5 == 4 and val % 10 < 9 else ""
        amount_13 = "" if val % 5 == 4 else (val % 5) * "I"

        return ''.join(amount_1 + amount_2 + amount_3 + amount_4 + amount_5 + amount_6 + amount_7 + amount_8
                       + amount_9 + amount_10 + amount_11 + amount_12 + amount_13)

    @staticmethod
    def from_roman(roman_num):
        number = 0
        if "IV" in roman_num:
            number += 4
        if "IX" in roman_num:
            number += 9
        if "IV" not in roman_num and "V" in roman_num:
            number += 5
        if "IV" not in roman_num and "I" in roman_num and "IX" not in roman_num:
            for i in roman_num:
                if i == "I":
                    number += 1
        if "XL" in roman_num:
            number += 40
        if "XC" in roman_num:
            number += 90
        if "X" in roman_num and "XL" not in roman_num and "XC" not in roman_num:
            for i in roman_num:
                if i == "X":
                    number += 10
            if "IX" in roman_num:
                number -= 10

        if "L" in roman_num and "XL" not in roman_num:
            number += 50
        if "CD" in roman_num:
            number += 400
        if "CM" in roman_num:
            number += 900
        if "C" in roman_num and "CM" not in roman_num and "CD" not in roman_num:
            for i in roman_num:
                if i == "C":
                    number += 100
            if "XC" in roman_num:
                number -= 100

        if "D" in roman_num and "CD" not in roman_num:
            number += 500
        if "M" in roman_num:
            for i in roman_num:
                if i == "M":
                    number += 1000
            if "CM" in roman_num:
                number -= 1000

        return number
