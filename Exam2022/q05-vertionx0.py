def SetVertDistance(G, S, x):
    if x in S:
        return 0
    paths = BFS(G, S)
    path = [x]
    currentNode = x
    while not (currentNode in S):
        if not (currentNode in paths):
            return -1

        currentNode = paths[currentNode]
        path.append(currentNode)
    path.reverse()
    return len(path)


def BFS(G, S):
    visitedNodes = []
    queue = S.copy()
    predecessorNodes = {}
    
    while queue:
        currentNode = queue.pop(0)
        visitedNodes.append(currentNode)
        for neighbor in G[currentNode]:
            if neighbor not in visitedNodes:
                queue.append(neighbor)
                predecessorNodes[neighbor] = currentNode
    print('paths', predecessorNodes)
    return predecessorNodes 

# TEST TEST TEST

testGraph = {
    '0': ['3','5','9'],
    '1': ['6','4'],
    '2': ['10','5'],
    '3': ['0'],
    '4': ['1','5', '8'],
    '5': ['2','0','4'],
    '6': ['1'],
    '7': [],
    '8': ['4'],
    '9': ['0'],
    '10': ['2']
}


print(SetVertDistance(testGraph, ['4','7'], '7'))
print(SetVertDistance(testGraph, ['0'], '3'))