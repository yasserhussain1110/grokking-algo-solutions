from queue import Queue


def bfs(graph, start, end):
    next = graph[start]
    q = Queue()
    for item in next:
        q.put(([start], item))
    visited = {start: True}
    while not q.empty():
        (path, item) = q.get()
        if item in visited:
            continue
        if item == end:
            path.append(item)
            return path
        else:
            copy_path = path[:]
            copy_path.append(item)
            if item in graph:
                for next_item in graph[item]:
                    q.put((copy_path, next_item))
        visited[item] = True
    return None


print(bfs({
    "a": ["b", "c"],
    "b": ["e"],
    "c": ["e", "d"],
    "d": ["e"]
}, "a", "e"))

print(bfs({
    "a": ["b", "c"],
    "b": ["e"],
    "c": ["e", "d"],
    "d": ["e"]
}, "a", "d"))

print(bfs({
    "a": ["b", "c"],
    "b": ["e"],
    "c": ["e", "d"],
    "d": ["e"]
}, "c", "b"))

print(bfs({
    "a": ["b", "c"],
    "b": ["e", "a"],
    "c": ["d", "e", "a"],
    "d": ["e", "c"],
    "e": ["b", "d"]
}, "c", "b"))
