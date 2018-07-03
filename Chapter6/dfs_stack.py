def dfs(graph, start, end):
    visited = {}
    stack = []
    stack.append(([], start))
    while len(stack) > 0:
        (path, node) = stack.pop()
        if node == end:
            path.append(end)
            return path
        if node not in visited:
            visited[node] = True
            if node in graph:
                for neighbour in graph[node]:
                    copy_path = path[:]
                    copy_path.append(node)
                    stack.append((copy_path, neighbour))
    return None


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
