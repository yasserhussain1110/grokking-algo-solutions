def knapsack(cost_graph, max_weight):
    items = list(cost_graph.keys())
    grid = [[([], 0) for i in range(max_weight + 1)] for j in items]
    for i in range(1, max_weight + 1):
        first_item = items[0]
        first_item_weight = cost_graph[first_item][0]
        if first_item_weight <= i:
            grid[0][i] = ([first_item], cost_graph[first_item][1])
    for i in range(1, len(items)):
        item = items[i]
        [weight, value] = cost_graph[item]
        for j in range(1, max_weight + 1):
            (prev_items, prev_value) = grid[i - 1][j]
            if j - weight < 1:
                alternate_value = value
                alternate_items = [item]
            else:
                (partial_items, partial_value) = grid[i - 1][j - weight]
                alternate_value = partial_value + value
                alternate_items = partial_items + [item]

            if alternate_value > prev_value and weight <= j:
                grid[i][j] = (alternate_items, alternate_value)
            else:
                grid[i][j] = grid[i - 1][j]
    return grid[-1][-1]


print(knapsack({
    "guitar": [1, 1500],
    "laptop": [3, 2000],
    "stereo": [4, 3000]
}, 4))
