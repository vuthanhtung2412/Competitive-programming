from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    plusOne = 0
    h1 = l1
    h2 = l2
    res = curr = ListNode()
    tmp = 0

    while h1 is not None and h2 is not None:
        tmp = h1.val + h2.val + plusOne
        if tmp >= 10:
            plusOne = 1
            curr.next = ListNode(tmp - 10)
        else:
            plusOne = 0
            curr.next = ListNode(tmp)

        curr = curr.next
        h1 = h1.next
        h2 = h2.next

    while h1:
        tmp = h1.val + plusOne
        if tmp >= 10:
            plusOne = 1
            curr.next = ListNode(tmp - 10)
        else:
            plusOne = 0
            curr.next = ListNode(tmp)

        curr = curr.next
        h1 = h1.next

    while h2:
        tmp = h2.val + plusOne
        if tmp >= 10:
            plusOne = 1
            curr.next = ListNode(tmp - 10)
        else:
            plusOne = 0
            curr.next = ListNode(tmp)

        curr = curr.next
        h2 = h2.next

    if plusOne:
        curr.next = ListNode(1)

    return res.next
