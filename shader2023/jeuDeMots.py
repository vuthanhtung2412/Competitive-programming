import sys

lines = ["fgexhgwad", "caailnw"
    , "avo"
    , "a"
    , "yez"
    , "ofgdmz"
    , "ibalebv"
    , "yvbyu"
    , "fehyoapkkp"
    , "sh"]

lines = ["ce"
,"tri"
,"bar"
,"banc"]

# sort by word length
# keep track of the word can be followed by adding
# enemy try to be on the even track, and we try to be on the odd track

l = sorted(lines[1:], key=len)
d = dict()

# build graph
for e in l:
    d[e[0]] = []

for e in l:
    if len(e) > 1:
        for i in range(1,len(e)+1):
            if e[:i] in d:
                d[e[:i]].append(e)

print(d)


def can_win(word, turn):
    # 1 is our turn
    # 0 is enemy turn
    if word not in d:
        if turn:
            return len(word) % 2
        else:
            return (len(word) % 2 + 1) % 2

    else:
        for w in d[word]:
            if can_win(w, (turn + 1) % 2):
                return False

        return True


letters = 'abcdefghijklmnopqrstuvwxyz'
res = []
for c in letters:
    if c in d and can_win(c, 1):
        res.append(c)

if res:
    for c in res:
        print(c)
else:
    print("impossible")
