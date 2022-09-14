# HasACycle is a function to check in UNDIRECTED graph has a cycle

def HasACycle(graph):
    color = {} # Holds colours of nodes 'W'hite = not visited, 'G'ray = visisted, 'B'lack = is a cycle
    parent = {}

    for u in graph.keys():
        color[u] = 'W'
        parent[u] = None

    hasACycle = False
    for u in graph.keys():
        if color[u] == 'W':
            hasACycle = dfs(graph, u, color, parent)
            if hasACycle == True:
                break
    return hasACycle     
    
# Helper function. DFS algorithm.
def dfs(graph, u, color, parent):
    color[u] = 'G' # Mark node as visited with Gray colour
    for v in graph[u]:
        if color[v] == 'W': # Check if node was not visited and run on in DFS
            parent[v] = u
            cycle = dfs(graph, v, color, parent) # DFS alg. on node/vertex to check if it is cycle itself
            if cycle == True: # If it was cycle, return True
                return True
        elif color[v] == "G" and parent[u]!=v : # Only in undirected graph : if node was visited, check if it sa parent of the node/vertek. If not. It must be cycle as it was already visited befofre
            color[u] = "B" 
            return True # Is a cycle
    return False
    

# TEST TEST TES

graph = {
    "A" : ["C", "B", "D"],
    "B" : ["A", "D"],
    "C" : ["A"],
    "D" : ["A","B" "E"],
    "E" : ["D"]
}

print(HasACycle(graph))
