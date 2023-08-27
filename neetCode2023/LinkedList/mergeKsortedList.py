from typing import Optional


class ListNode:
    def __init__(self, val=0, nex=None):
        self.val = val
        self.next = nex


def lst2link(lst):
    if lst:
        cur = dummy = ListNode(lst[0])
        for e in lst[1:]:
            cur.next = ListNode(e)
            cur = cur.next
        return dummy
    else:
        return None


def MyPrintLinkedList(l: Optional[ListNode]):
    h = l
    res = []
    while h is not None:
        res.append(h.val)
        h = h.next
    print(res)


def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    res = None
    mi = 1e4

    # for i in range(len(lists)):
    #     if lists[i] is None:
    #         lists.pop(i)

    # correct way to modify a list iteratively
    lists = [node for node in lists if node]

    for i in range(len(lists)):
        if lists[i].val < mi:
            mi = lists[i].val
            res = lists[i]

    res = ListNode(-1e4, res)
    curr = res

    while lists:
        mini = 1e4
        miId = 0
        for i in range(len(lists)):
            if lists[i].val <= mini:
                mini = lists[i].val
                miId = i

        curr.next = lists[miId]
        curr = curr.next
        lists[miId] = lists[miId].next

        # filter an array with a loop
        lists = [node for node in lists if node]

    return res.next
