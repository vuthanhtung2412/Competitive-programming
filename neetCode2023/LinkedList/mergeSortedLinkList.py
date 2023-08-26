from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def lst2link(lst):
    if lst:
        cur = dummy = ListNode(lst[0])
        for e in lst[1:]:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy
    else:
        return None


def printLinkedList(l: Optional[ListNode]):
    h = l
    res = []
    while h is not None:
        res.append(h.val)
        h = h.next
    print(res)


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    h1 = list1
    h2 = list2

    res = None
    if list1.val <= list2.val:
        res = list1
    else:
        res = list2

    while True:
        if h1.val <= h2.val:
            while h1.next is not None and h1.next.val <= h2.val:
                h1 = h1.next
            if h1.next is None:
                h1.next = h2
                return res
            else:
                tmp = h1.next
                h1.next = h2
                h1 = tmp
        else:
            while h2.next is not None and h2.next.val <= h1.val:
                h2 = h2.next
            if h2.next is None:
                h2.next = h1
                return res
            else:
                tmp = h2.next
                h2.next = h1
                h2 = tmp


print([1][1:])
printLinkedList(lst2link([1, 5, 7]))
printLinkedList(mergeTwoLists(lst2link([1, 2, 4, 182, 200, 200, 289, 291]), lst2link([1, 3, 4, 18, 192, 6483])))
printLinkedList(mergeTwoLists(lst2link([]), lst2link([])))
printLinkedList(mergeTwoLists(lst2link([]), lst2link([0])))
