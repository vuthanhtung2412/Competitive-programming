# *******
# * Read input from STDIN
# * Use print to output your result to STDOUT.
# * Use sys.stderr.write() to display debugging information to STDERR
# * ***/
import sys

lines = ["ce"
    , "tri"
    , "bar"
    , "banc"]


class TrieNode:
    def __init__(self, val=""):
        self.val = val
        self.children = []


def build(node, s):
    if s:
        notChild = True
        for n in node.children:
            if n.val == s[0]:
                notChild = True
                build(n, s[1:])

        if notChild:
            node.children.append(TrieNode(s[0]))
            build(node.children[-1], s[1:])


nodes = []

# Build graph
l = sorted(lines[1:], key=len)
for e in l:
    nodes.append(TrieNode(e[0]))

for e in l:
    for n in nodes:
        if n.val == e[0]:
            build(n, e[1:])


def can_win(node):
    for n in node.children:
        if can_win(n):
            return False
    return True


res = []
for n in nodes:
    if can_win(n):
        res.append(n.val)

if res:
    for c in sorted(res):
        print(c)
else:
    print("impossible")
