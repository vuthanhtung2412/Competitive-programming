def calcEquation(equations, values, queries):
    """
    :type equations: List[List[str]]
    :type values: List[float]
    :type queries: List[List[str]]
    :rtype: List[float]
    """
    graph = dict()
    for i in range(len(equations)):
        edges = graph.get(equations[i][0], {})
        edges[equations[i][1]] = values[i]
        graph[equations[i][0]] = edges

        edges = graph.get(equations[i][1], {})
        edges[equations[i][0]] = 1 / values[i]
        graph[equations[i][1]] = edges
    res = []
    for q in queries:
        if q[0] not in graph or q[1] not in graph:
            res.append(-1)
        else:
            res.append(self.query(graph, q[0], q[1]))
    return res


def query(graph, start, dest):
    visited = set()
    return dfs(graph, start, dest, visited)


# DFS implementation
def dfs(graph, node, target, visited):
    if node == target:
        return 1
    if node not in visited:
        visited.add(node)
        for neighbor, coeff in graph[node].items():
            tmp = dfs(graph, neighbor, target, visited)
            if tmp != -1:
                return coeff * tmp
    return -1


print(
    calcEquation(
        [["a", "b"], ["b", "c"], ["bc", "cd"]],
        [1.5, 2.5, 5.0],
        [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]],
    )
)  # [3.75000,0.40000,5.00000,0.20000]
