from typing import List


# it seems quite optimized to me
def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    # Sort emails of each account first, this sort make the union operation complexity only O(n) instead of O(nlog(n))
    # deque = double-end list
    # time complexity of converting deque to list is O(n)
    for i in range(len(accounts)):
        accounts[i] = [accounts[i][0]] + sorted(list(set(accounts[i][1:])))

    # Union find, union not only modify the parents list but also merge account
    # Perform union find only for account with the same name
    dmail = {}
    dname = {}
    parents = [i for i in range(len(accounts))]

    for i in range(len(accounts)):
        if accounts[i][0] in dname:
            dname[accounts[i][0]].append(i)
        else:
            dname[accounts[i][0]] = [i]

    def find(x):
        if parents[x] == x:
            return x
        else:
            return find(parents[x])

    def union(x, y):
        # merge group of x into group of y
        px = find(x)
        py = find(y)
        parents[px] = py

        if accounts[px][0] != accounts[py][0]:
            raise Exception("the test case is bullshit"
                            )
        tmp = [accounts[px][0]]
        xp = 1  # pointer for group x
        yp = 1  # pointer for group y
        while xp < len(accounts[px]) and yp < len(accounts[py]):
            if accounts[px][xp] < accounts[py][yp]:
                tmp.append(accounts[px][xp])
                xp += 1
            elif accounts[px][xp] == accounts[py][yp]:
                tmp.append(accounts[px][xp])
                xp += 1
                yp += 1
            else:
                tmp.append(accounts[py][yp])
                yp += 1

        if yp < len(accounts[py]):
            while yp < len(accounts[py]):
                tmp.append(accounts[py][yp])
                yp += 1
        else:
            while xp < len(accounts[px]):
                tmp.append(accounts[px][xp])
                xp += 1

        accounts[py] = tmp

    # Union find without group by name
    """
    for i in range(len(accounts)):
        for mail in accounts[i][1:]:
            if mail in dmail:
                union(i, dmail[mail])
            else:
                dmail[mail] = i
    """

    # Union find with group by name
    for k, vs in dname.items():
        for v in vs:
            for mail in accounts[v][1:]:
                if mail in dmail:
                    union(v, dmail[mail])
                else:
                    dmail[mail] = v
            # print(dmail)
        dmail.clear()

    res = []
    for i in range(len(parents)):
        if i == parents[i]:
            res.append(accounts[i])

    return res


# Idea to optimize not union at every step but only union when we have the final parent list, I can save all the mail in a list
# turn out to be not very optimized in terms of space nor time complexity
def accountsMerge2(accounts: List[List[str]]) -> List[List[str]]:
    # Sort emails of each account first, this sort make the union operation complexity only O(n) instead of O(nlog(n))
    # deque = double-end list
    # time complexity of converting deque to list is O(n)
    mailSet = []
    for acc in accounts:
        mailSet.append(set(acc[1:]))

    # Union find, union not only modify the parents list but also merge account
    # Perform union find only for account with the same name
    dmail = {}
    dname = {}
    parents = [i for i in range(len(accounts))]

    for i in range(len(accounts)):
        if accounts[i][0] in dname:
            dname[accounts[i][0]].append(i)
        else:
            dname[accounts[i][0]] = [i]

    def find(x):
        if parents[x] == x:
            return x
        else:
            return find(parents[x])

    def union(x, y):
        # merge group of x into group of y
        px = find(x)
        py = find(y)
        parents[px] = py

        if accounts[px][0] != accounts[py][0]:
            raise Exception("the test case is bullshit")

        for m in mailSet[px]:
            mailSet[py].add(m)

    # Union find with group by name
    for k, vs in dname.items():
        for v in vs:
            for mail in accounts[v][1:]:
                if mail in dmail:
                    union(v, dmail[mail])
                else:
                    dmail[mail] = v
            # print(dmail)
        dmail.clear()

    res = []
    for i in range(len(parents)):
        if i == parents[i]:
            res.append([accounts[i][0]] + sorted(list(mailSet[i])))

    return res


# TODO: watch the optimized solution on YT
# store all the email in a dictionary then aggregate later by iterate through the list of emails
def ncAccountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    pass

print(accountsMerge(
    [["Alex", "Alex5@m.co", "Alex4@m.co", "Alex0@m.co"], ["Ethan", "Ethan3@m.co", "Ethan3@m.co", "Ethan0@m.co"],
     ["Kevin", "Kevin4@m.co", "Kevin2@m.co", "Kevin2@m.co"], ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe2@m.co"],
     ["Gabe", "Gabe3@m.co", "Gabe4@m.co", "Gabe2@m.co"]]))
# this bug because the initial list could contain duplicate emails

print(accountsMerge2(
    [["Alex", "Alex5@m.co", "Alex4@m.co", "Alex0@m.co"], ["Ethan", "Ethan3@m.co", "Ethan3@m.co", "Ethan0@m.co"],
     ["Kevin", "Kevin4@m.co", "Kevin2@m.co", "Kevin2@m.co"], ["Gabe", "Gabe0@m.co", "Gabe3@m.co", "Gabe2@m.co"],
     ["Gabe", "Gabe3@m.co", "Gabe4@m.co", "Gabe2@m.co"]]))
