graph = {
    0: [1, 2],
    1: [3],
    2: [],
    3: []
}

visited = set()
stack = [0]

while stack:
    node = stack.pop()

    if node not in visited:
        print(node)
        visited.add(node)

        for neighbor in graph[node]:
            stack.append(neighbor)