from collections import deque
# Used that one to check if 2 el. are in the same connected component
# This is my function from CW#3

def SetVertDistance(G, S, x):
    # check if all elements of S are in the same connected components as x
    for i in range(0, len(S)):
        if checkIfConnectedComponents(G, S[i], x) == False:
            return -1 # Element of S in not in the same con.comp. as x. return -1
        
    # Find shortest path between any el of S and x
    pathsLengths = [] # will hold all paths lengts to determine shortest one win 'min'
    for i in range(0, len(S)):
        pathsLengths.append(BfsShortestPath(G, S[i], x)) # Get all shoretest paths from ech. el of S to x
    return min(pathsLengths) # return minimal path length
    
    
    
# Helper: To find if vertices are in the same connected component. Used in Cw3
def checkIfConnectedComponents(adjacencyList, vertexX, vertexY):
    if vertexX == vertexY:
        return True
    if vertexX > len(adjacencyList) or vertexY > len(adjacencyList):
        return False
    visitedVertices = [False] * len(adjacencyList)
    queue = deque()
    visitedVertices[vertexX] = True
    queue.append(vertexX)
    while len(queue) > 0:
        k = queue.popleft()
        for j in adjacencyList[k]:
            if j == vertexY:
                return True
            if not visitedVertices[j]:
                visitedVertices[j] = True
                queue.append(j)
    visitedVertices = [False] * len(adjacencyList)
    queue = deque()
    visitedVertices[vertexY] = True
    queue.append(vertexY)
    while len(queue) > 0:
        k = queue.popleft()
        for j in adjacencyList[k]:
            if j == vertexX:
                return True
            if not visitedVertices[j]:
                visitedVertices[j] = True
                queue.append(j)
    return False

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
    return len(shortestPath(predecessorNodes, startNode, endNode))

def shortestPath(predecessorNode, startNode, endNode):
    path = [endNode]
    currentNode = endNode
    while currentNode != startNode:
        currentNode = predecessorNode[currentNode]
        path.append(currentNode)
    path.reverse()
    return path


# TESTS 
graph = [
        [3],
        [0, 2],
        [0],
        [4],
        [],
        [6],
        []
    ]


L = ['0','3']
x = 0

print("Just check if x in in connected compinent with ant el of S :")
print(checkIfConnectedComponents(graph, 3, 0)) # T
print(checkIfConnectedComponents(graph, 1, 2)) # T
print(checkIfConnectedComponents(graph, 1, 5)) # F
print(checkIfConnectedComponents(graph, 5, 6)) # T
print(checkIfConnectedComponents(graph, 2, 6)) # F

print("\n Actual function: \n")
print(SetVertDistance(graph, L, x))
