# Check if graph walk visits all vertices
# Solution:
def WalkAllVertices(A, L):
    # If L has less vertices than len of graph = False
    if len(L) < len(A):
        return False
    # Test if it is a walk
    if IsWalk(A, L) == False:
        return False
    
    # Track all visited vertices in a list
    VisitedVertices = [0] * len(A)
    
    # Walk all el in L and insert 1 in VisitedVertices into corresponding
    # index, to mark as vertice was visited
    for i in range(0, len(L)):
        if VisitedVertices[L[i]] == 0:
            VisitedVertices[L[i]] = 1
    # If any 0 exists in VisitedVertices, mean not all vertices were visited
    return not 0 in VisitedVertices
########## END OF ACTUAL FUNCTION #################

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
graphA = [
    [0, 1, 0, 1, 0], 
    [1, 0, 0, 1, 1], 
    [0, 0, 0, 1, 0],
    [1, 1, 1, 0, 0], 
    [0, 1, 0, 0, 0]
]

L1 = [2, 3, 0, 1, 4]  # True: walk with visiting all vertices
L2 = [2, 3, 1, 4]  # False: walk but not visiting all vertices
L3 = [2, 3, 1, 4, 0]  # False:  visits all vertices but not a walk

print(WalkAllVertices(graphA, L1)) # T
print(WalkAllVertices(graphA, L2)) # T
print(WalkAllVertices(graphA, L3)) # F