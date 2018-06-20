def dfs(graph, start, end, visited=None):
    if not visited: visited = {}
    visited[start] = True
    if start == end: return [end]
    if start not in graph: return None
    neighbours = graph[start]
    neighbour_paths = list(
        filter(
            lambda x: x is not None,
            [dfs(graph, neighbour, end, visited) for neighbour in neighbours if neighbour not in visited]
        )
    )
    if len(neighbour_paths) == 0: return None
    smallest_path = min(neighbour_paths)
    return [start] + smallest_path


print(dfs({
    "a": ["b", "c"],
    "b": ["e"],
    "c": ["e", "d"],
    "d": ["e"]
}, "a", "e"))

print(dfs({
    "a": ["b", "c"],
    "b": ["e"],
    "c": ["e", "d"],
    "d": ["e"]
}, "a", "d"))

print(dfs({
    "a": ["b", "c"],
    "b": ["e"],
    "c": ["e", "d"],
    "d": ["e"]
}, "c", "b"))

print(dfs({
    "a": ["b", "c"],
    "b": ["e", "a"],
    "c": ["d", "e", "a"],
    "d": ["e", "c"],
    "e": ["b", "d"]
}, "c", "b"))
