import copy
import math
from functools import reduce
from typing import List


def testEncodingChar():
    print(format(ord("?"), "x"))  # hexadecimal
    print(ord('c'))  # Unicode point which is an integer


def deepShallowCopy():
    # Original nested list
    original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], (4, 6, 9), "dmm", 9]

    # Shallow copy
    shallow_copied_list = copy.copy(original_list)
    ref_2_original_obj = original_list  # different from shallow copy
    # shallow_copied_list = copy.copy(original_list)

    # Deep copy
    deep_copied_list = copy.deepcopy(original_list)

    # check id (address in heap)

    print("test list obj (mutable/non primitive)")
    print(id(original_list[0][0]) == id(shallow_copied_list[0][0]))
    print(id(original_list[0]) == id(shallow_copied_list[0]))
    print(id(original_list[0][0]) == id(deep_copied_list[0][0]))
    print(id(original_list[0]) == id(deep_copied_list[0]))

    print("test tuple (non primitive / non mutable)")
    print(id(original_list[3]) == id(deep_copied_list[3]))
    print(id(original_list[3]) == id(shallow_copied_list[3]))
    original_list[3] = (3, 4)
    print(id(original_list[3]) == id(deep_copied_list[3]))
    print(id(original_list[3]) == id(shallow_copied_list[3]))

    print("test string (primitive / non mutable")
    print(id(original_list[4]) == id(deep_copied_list[4]))
    print(id(original_list[4]) == id(shallow_copied_list[4]))
    original_list[4] = "dep trai"
    print(id(original_list[4]) == id(deep_copied_list[4]))
    print(id(original_list[4]) == id(shallow_copied_list[4]))

    print("test int (primitive / non mutable)")
    print(id(original_list[5]) == id(deep_copied_list[5]))
    print(id(original_list[5]) == id(shallow_copied_list[5]))
    original_list[5] = 10
    print(id(original_list[5]) == id(deep_copied_list[5]))
    print(id(original_list[5]) == id(shallow_copied_list[5]))

    # For both shallow and deep copy
    # new NON MUTABLE obj will be created if change in original list happen

    # for deep copy
    # new MUTABLE obj will be created at the time of initialization of new list, dict, set
    # shallow copy only take the address of mutable obj

    # Modify the original list
    original_list[0][0] = 100

    # Print all three lists
    print("Original List:", original_list)
    print("Shallow Copied List:", shallow_copied_list)
    print("Deep Copied List:", deep_copied_list)
    print(id(original_list[0][0]) == id(deep_copied_list[0][0]))


def interDict():
    d = {1: 2, 3: 3}
    for i in d:  # this will only print out the key
        print(i)
    for k, v in d.items():
        print(k)
        print(v)


def testXOR():
    for i in range(2):
        for j in range(2):
            print("%s xor %s = %s" % (i, j, i ^ j))


# Test python decorator
def my_decorator(func):
    # TODO: print all params of func
    def wrapper():
        func()

    return wrapper


@my_decorator
def say_whee():
    print("Whee!")


# Sort with cmp and sort with key
def customSort():
    l = [6, 8, 10, 23, -4, -7]
    # sorted_l = sorted(l, cmp=lambda x, y: x ** 3 - y ** 3)
    # cmp is removed in python 3
    sorted_l = sorted(l, key=lambda x: x ** 3)  # Sort with key
    print(sorted_l)

    l = [(3, 'aaa'), (1, 'bbbb'), (3, 'ab'), (2, 'aaa')]
    # Sort on 1st element then second elmenent
    l = sorted(l, key=lambda x: (x[0], x[1]))
    print(l)


def mutableString():
    """Mutable string for concatenation O(n) instead of O(m+n)"""
    # TODO : implement a mutable string
    pass


# nonlocal vs globals
def outer_function():
    """nonlocal : used inside nested functions to indicate that a variable from an enclosing (non-global) scope is being accessed or modified."""
    x = 10

    def inner_function():
        nonlocal x  # Declare x as a nonlocal variable
        x += 1

    inner_function()
    print(x)  # Prints 11


x = 10


def modify_global():
    """global : The global keyword is used to indicate that a variable is being accessed or modified in the global scope, which is outside any function."""
    global x  # Declare x as a global variable
    x += 1


def docstring():
    """dmm"""
    print(docstring.__doc__)


def iterateReversed():
    """2 ways to iterate backward"""
    for i in range(10, 0, -1):
        print(i)
    print("-----")
    for i in reversed(range(10)):
        print(i)


def testReduce():
    arr = [3, 6, 7, 11]

    time = 0
    for b in arr:
        time += math.ceil(b / 6)
    print(time)  # 6

    print(reduce(lambda x, y: math.ceil(x / 6) + math.ceil(y / 6), arr))  # 3
    # explanation
    # they reduce the result of previous reduction
    # ceil((ceil((ceil(3/6) + ceil(6/6)) / 6) + ceil(7/6)) / 6) + ceil(11/6)


# Complexity of len() function is O(1)

def checkKeyExist():
    dic = {}
    if "key" in dic:
        print("key existed")
    else:
        print("key non existing")

    try:
        if dic["key"]:
            print(dic["key"])
        else:
            print(None)
    except KeyError:
        print("key error")


def testTryCatch():
    # TODO
    pass


arr = [x for x in range(10)]


def testRefOrCopy(l: List[int]):  # pass reference instead of a copy
    l[8] = 2


# testRefOrCopy(arr)
# print(arr)

def testForModif():
    a = [1, 2, 3, 4, 5]
    for i in a:
        # miss number 3 because the rest of the array after 2 is shifted
        # i is a pointer to the memory
        print(i)
        if i == 2:
            a.remove(i)

    a = [i for i in range(10)]
    print("--------------")
    for i in range(len(a)):  # len(a) returns an integer
        print(a[i])  # index error
        if a[i] == 3 or a[i] == 6:
            a.pop(i)

    print(a)


# testForModif()

import numpy as np


def dotProductVsMatmul():
    a = np.full((9, 3, 6, 3), 1)
    b = np.full((7, 8, 3, 5), 1)
    d = np.dot(a, b)

    print(d)
    print(d.shape)  # (9, 3, 6, 7, 8, 5)
    # 1 a.shape[-1]-D vector of matrix a matmul with a matrix of dim b.shape[-2]*b.shape[-1] then stack subsequently by other dimension of b then a

    a = np.full((9, 8, 6, 3), 1)
    b = np.full((9, 8, 3, 4), 1)
    c = np.matmul(a, b)
    print(c)
    print(c.shape)  # (9, 8, 6, 4)

    try:
        a = np.full((9, 8, 6, 3, 9), 1)
        b = np.full((9, 8, 3, 4, 9), 1)
        c = np.matmul(a, b)
        print(c)
    except:
        print("this bug")
    # flatten other dimension except for the last 2 we then obtain a stack of matrix, perform matrix multiplication accordingly then reshape


def filterWLiComprehension():
    print([num ** 2 for num in range(10) if num % 2 == 0])


# deque.popleft() is O(1) -- a constant time operation. While list.pop(0) is O(n)
def dequePython():
    pass


import re


def regex():
    # Example input string
    input_string = "My email address is john.doe@example.com, and my phone number is 123-456-7890."

    # Define a regex pattern with capturing groups
    # "r" in front of a string literal, it indicates a raw string. A raw string is a string that treats backslashes (\) as literal characters and not as escape characters.
    email_pattern = r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'
    phone_pattern = r'(\d{3})-(\d{3}-\d{4})'

    # Use re.findall to extract matches
    emails = re.findall(email_pattern, input_string)
    phones = re.findall(phone_pattern, input_string)

    # Print a list of extracted variables
    print("Emails:", emails)
    # ['john.doe@example.com'] because there is only one big group
    print("Phone numbers:", phones)
    # return [('123', '456-7890')] tuples of groups

    # LAZY matching
    string = "aabqekjlkjavabdfabb"
    pattern = r"a.*?b"
    res = re.findall(pattern, string)
    print(res)

    # LOOKAHEAD & LOOKBEHIND
    string = "abc123"
    pattern = r"(?<=[A-Za-z])\d+"
    res = re.findall(pattern, string)
    print(res)

    string = "123456"
    pattern = "\d?(?=\d{4})"
    res = re.findall(pattern, string)
    print(res)

    # GROUPs

    # Use re.search to find the first match
    match = re.search(phone_pattern, input_string)

    if match:
        # print the whole sequence
        print(match.group(0))

        # Extract the first 3 numbers into one variable
        print(match.group(1))

        # Extract the other 7 numbers into another variable
        print(match.group(2))


from drawtree import draw_level_order


def draw_tree():
    draw_level_order('[4,-7,-3,#,#,-9,-3,9,-7,-4,#,6,#,-6,-6,#,#,0,6,5,#,9,#,#,-1,-4,#,#,#,-2]')


def nonIntLoop():
    for i in range(1, 10, 3):
        print(i)


nonIntLoop()
