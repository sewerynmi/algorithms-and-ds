# Write a function whose input is an adjacency matrix A of a graph G and a list
# L whose elements are vertices of G (possibly with repetitions). The function
# should return true if L is a path and f alse otherwise.
# The runtime of the function should be O(len(L)).
# Hint: you may need to modify the adjacency matrix during the exploration of L.

# Answer. As in the case of trail, we first need to check whether L is a walk.
# For checking of non-repetition of vertices, we introduce a list visited of length
# n all elements of which are initially zeroes. Then the list L is explored in a
# loop. Let curvert be the current vertex. If visited[curvert] is 1 this means that
# this vertex has been observed by the loop during one of the previous iterations.
# Hence, f alse can be returned imediately. Otherwise, visited[curvert] is set to
# 1. true is returned after the loop.

def IsPath(A, L):
    if IsWalk(A, L) == False:
        return False
    visitedVertices = [0] * len(A)
    for i in range (0, len(L)):
        currentVertice = L[i]
        if visitedVertices[currentVertice] == 1:
            return False
        visitedVertices[currentVertice] = 1
    return True
    
    
# Helper from file 01-is-a-graph-walk.py
# To check if is set of vertices is a walk.
def IsWalk(A, L):
    for i in range(1, len(L)):
        currentVertice = L[i]
        previousVertice = L[i-1]
        #print("checking vertices = [i][j]:", currentVertice, ",", previousVertice)
        if A[currentVertice][previousVertice] == 0:
            return False
    return True

# TEST TEST TEST
print("\nTest Path\n")
graphA = [
    [0, 1, 0, 1],
    [1, 0, 1, 1],
    [0, 1, 0, 1],
    [1, 1, 1, 0]
]

pathA = [0, 1, 2, 3, 1] # False, repeated vertice 1
pathB = [0, 1, 2, 3, 1, 0] # False , not a Trail, repeated edge 0-1 , 1-0
pathC = [0, 1 , 2, 3] # True

print(IsPath(graphA, pathA)) # False
print(IsPath(graphA, pathB)) # False
print(IsPath(graphA, pathC)) # True
