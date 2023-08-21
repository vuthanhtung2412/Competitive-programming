import copy


def testEncodingChar():
    print(format(ord("?"), "x"))  # hexadecimal
    print(ord('c'))  # Unicode point which is an integer


def deepShallowCopy():
    # Original nested list
    original_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    # Shallow copy
    shallow_copied_list = copy.copy(original_list)
    # shallow_copied_list = copy.copy(original_list)

    # Deep copy
    deep_copied_list = copy.deepcopy(original_list)

    # check id (address in heap)
    print(id(original_list[0][0]) == id(shallow_copied_list[0][0]))
    print(id(original_list[0]) == id(shallow_copied_list[0]))
    print(id(original_list[0][0]) == id(deep_copied_list[0][0]))
    print(id(original_list[0]) == id(deep_copied_list[0]))

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
