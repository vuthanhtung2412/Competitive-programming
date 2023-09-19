from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val


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


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    # maintain 2 pointers can reduce exec time by a half
    res = l = ListNode(0, head)
    r = head
    for i in range(n):
        r = r.next

    while r is not None:
        l = l.next
        r = r.next

    l.next = l.next.next

    return res.next


printLinkedList(removeNthFromEnd(lst2link([x for x in range(10)]), 4))
