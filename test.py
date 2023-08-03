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
    for k,v in d.items():
        print(k)
        print(v)
