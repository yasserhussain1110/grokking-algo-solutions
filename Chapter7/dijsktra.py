def find_cheapest_node(cost_graph, processed):
    (cheapest_node, cheapest_cost) = (None, float("inf"))
    for node, cost in cost_graph.items():
        if cost < cheapest_cost and node not in processed:
            cheapest_cost = cost
            cheapest_node = node
    return cheapest_node


def dijsktra(graph, start, finish):
    cost_graph = graph[start].copy()
    parent_graph = {node: start for node in graph[start]}
    processed = []
    while len(processed) != len(cost_graph.keys()):
        cheap = find_cheapest_node(cost_graph, processed)
        for node, cost in graph[cheap].items():
            new_cost = cost + cost_graph[cheap]
            if node not in cost_graph or new_cost < cost_graph[node]:
                cost_graph[node] = new_cost
                parent_graph[node] = cheap
        processed.append(cheap)

    current = finish
    path = [current]
    while current != start:
        if current not in parent_graph:
            return None
        path.insert(0, parent_graph[current])
        current = parent_graph[current]

    return path


print(dijsktra({
    "START": {
        "A": 6,
        "B": 2
    },
    "A": {
        "FIN": 1
    },
    "B": {
        "A": 3,
        "FIN": 5
    },
    "FIN": {}
}, "START", "FIN"))

print(dijsktra({
    "START": {
        "A": 6,
        "B": 2
    },
    "A": {
        "FIN": 1
    },
    "B": {
        "A": 3,
        "FIN": 5
    },
    "FIN": {}
}, "START", "A"))

print(dijsktra({
    "START": {
        "A": 6,
        "B": 2
    },
    "A": {
        "FIN": 1
    },
    "B": {
        "A": 3,
        "FIN": 5
    },
    "FIN": {}
}, "A", "B"))

print("------------------------------------Exercises------------------------------------")

print(dijsktra({
    "START": {
        "A": 5,
        "B": 2
    },
    "A": {
        "C": 4,
        "D": 2
    },
    "B": {
        "A": 8,
        "D": 7
    },
    "C": {
        "FINISH": 3,
        "D": 6
    },
    "D": {
        "FINISH": 1
    },
    "FINISH": {}
}, "START", "FINISH"))

print(dijsktra({
    "START": {
        "A": 10
    },
    "A": {
        "C": 20
    },
    "B": {
        "A": 1
    },
    "C": {
        "FINISH": 30,
        "B": 1
    },
    "FINISH": {}
}, "START", "FINISH"))
