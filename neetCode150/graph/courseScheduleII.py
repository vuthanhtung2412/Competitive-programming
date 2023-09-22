from typing import List


def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    graph = [[] for _ in range(numCourses)]

    for e in prerequisites:
        graph[e[0]].append(e[1])

    findRequirements = [0] * numCourses  # keep track of upper node on dps
    visited = [0] * numCourses  # keep track of valid node
    res = True
    topological_order = []

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
                topological_order.append(i)

    for i in range(numCourses):
        if not visited[i]:
            dfs(i)
        if not res:
            return []

    return topological_order
