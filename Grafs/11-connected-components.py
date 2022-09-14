from collections import deque

def connected_components(graph):
    seen = set()

    for root in range(len(graph)):
        if root not in seen:
            seen.add(root)
            component = []
            queue = deque([root])

            while queue:
                node = queue.popleft()
                component.append(node)
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)
            yield component
            
graph = [
    [1, 2, 3],  # neighbors of node "0"
    [0, 2],     # neighbors of node "1"
    [0, 1],     # ...
    [0, 4, 5],
    [3, 5],
    [3, 4, 7],
    [8],
    [5],
    [9, 6],
    [8]
]

print(list(connected_components(graph)))  # [[0, 1, 2, 3, 4, 5, 7], [6, 8, 9]]