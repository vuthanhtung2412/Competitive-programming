from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    # course not possible if there is loop
    # topological sort to detect loop

    graph = [[] for _ in range(numCourses)]
    # graph = [list()] * numCourses # a list of n pointer to the same obj

    for e in prerequisites:
        graph[e[0]].append(e[1])

    findRequirements = [0] * numCourses  # keep track of upper node on dps
    visited = [0] * numCourses # keep track of valid node
    res = True

    def dfs(i: int):
        if not visited[i]:
            nonlocal res
            if findRequirements[i]:
                res = False
                return
            else:
                findRequirements[i] = 1
                for c in graph[i]:
                    dfs(c)
                    if not res:
                        return
                findRequirements[i] = 0
                visited[i] = 1

    for i in range(numCourses):
        if not visited[i]:
            dfs(i)
        if not res:
            return False

    return res


print(canFinish(2, [[1, 0]]))
