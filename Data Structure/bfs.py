from collections import deque

graph = {
    0: [1, 2],
    1: [3],
    2: [],
    3: []
}

visited = set()
queue = deque([0])   # start from node 0

while queue:
    node = queue.popleft()   # first in, first out

    if node not in visited:
        print(node)
        visited.add(node)

        for neighbor in graph[node]:
            queue.append(neighbor)