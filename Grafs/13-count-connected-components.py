
def countComponents(graph):
    count = 0
    visited = set()
    for node in graph:
        if traverse(graph,node,visited) == True:
            count+=1
    return count
def traverse(graph,current,visited):
    if current in visited:
        return False
    visited.add(current)
    for neighbor in graph[current]:
        traverse(graph, neighbor,visited)
    return True   

graph = {
    'a': ['c', 'b'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': [],
    'g':[]
}

print(countComponents(graph))