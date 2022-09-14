def BfsShortestPath(graph, startNode, endNode):
    visitedNodes = []
    queue = [startNode]
    predecessorNodes = {}
    
    while queue:
        currentNode = queue.pop(0)
        visitedNodes.append(currentNode)
        for neighbor in graph[currentNode]:
            if neighbor not in visitedNodes:
                queue.append(neighbor)
                predecessorNodes[neighbor] = currentNode
    print('paths', predecessorNodes)
    return len(shortestPath(predecessorNodes, startNode, endNode))

def shortestPath(predecessorNode, startNode, endNode):
    path = [endNode]
    currentNode = endNode
    while currentNode != startNode:
        currentNode = predecessorNode[currentNode]
        path.append(currentNode)
    path.reverse()
    return path
    
    
# TEST TEST TEST

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

#print(list(connected_components(graph)))  # [[0, 1, 2, 3, 4, 5, 7], [6, 8, 9]]


L = ['0', '2', '3']

print(BfsShortestPath(graph, '0', '1'))