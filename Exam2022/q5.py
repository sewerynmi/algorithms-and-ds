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
    return shortestPath(predecessorNodes, startNode, endNode)

def shortestPath(predecessorNode, startNode, endNode):
    path = [endNode]
    currentNode = endNode
    while currentNode != startNode:
        currentNode = predecessorNode[currentNode]
        path.append(currentNode)
    path.reverse()
    return path


def SetVertDistance(G, S, x):
    if x in S:
        return 0

    shortest_path_length = 10000
    for s in S:
        path = BfsShortestPath(G, s, x)
        print ("Source :", s, "Destination :", x, "Path :", path)
        if path[-1] == x:   # Then path found between s and x
            if len(path) < shortest_path_length:
                shortest_path_length = len(path)
                
    if shortest_path_length == 10000:   # Then not found any path and assign -1 to shortest_path_length
        shortest_path_length = -1
        
    return shortest_path_length

G = {
    '0': ['3','5','9'],
    '1': ['6','7','4'],
    '2': ['10','5'],
    '3': ['0'],
    '4': ['1','5', '8'],
    '5': ['2','0','4'],
    '6': ['1'],
    '7': ['1'],
    '8': ['4'],
    '9': ['0'],
    '10': ['2']
}

S = ('1','2','3','4','5')

x = '10'

print(SetVertDistance(G, S, x))

#print(BfsShortestPath(G, '10', '3'))



##for s in S:
##    print (s)
##
##print (5 in S)
