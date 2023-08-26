from typing import Optional


class Node:
    def __init__(self, x: int, nex: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = nex
        self.random = random


def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
    # Ruined the original list
    curr = head
    res = prev = Node(0)

    while curr is not None:
        copy = Node(curr.val, None, curr.random)
        prev.nex = copy
        prev = prev.nex

        tmp = curr.next
        curr.next = copy
        curr = tmp

    h = res
    while h is not None:
        if h.random:
            h.random = h.random.next
        h = h.next

    return res.next


def copyRandomListInterweave(head: 'Optional[Node]') -> 'Optional[Node]':
    # Old List: A --> B --> C --> D InterWeaved List: A --> A' --> B --> B' --> C --> C' --> D --> D'
    # can reconstruct the original list
    # TODO
    pass
