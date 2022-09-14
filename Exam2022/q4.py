import math
def LogWalk(A, L):
    # Test if it is a walk
    if IsWalk(A, L) == False:
        return False # If not a walk, skip
    # Track all visited vertices in a list
    VisitedVertices = [0] * len(A)
    # Walk all el in L and insert 1 in VisitedVertices into corresponding
    # index, to mark as vertice was visited
    for i in range(0, len(L)):
        if VisitedVertices[L[i]] == 0:
            VisitedVertices[L[i]] = 1
    #print (VisitedVertices.count(1))
    return VisitedVertices.count(1) < math.log(math.pow(len(graphA),2)) ## retrurn True if num of visited vertices is log(len(A))


def IsWalk(A, L):
    for i in range(1, len(L)):
        currentVertice = L[i]
        previousVertice = L[i-1]
        if A[currentVertice][previousVertice] == 0:
            return False
    return True
    
graphA = [
    [0, 1, 0, 1, 0], 
    [1, 0, 0, 1, 1], 
    [0, 0, 0, 1, 0],
    [1, 1, 1, 0, 0], 
    [0, 1, 0, 0, 0]
]

L1 = [2, 3, 0, 1, 4]  # True: walk with visiting all vertices
L2 = [2, 3, 1]  # False: walk but not visiting all vertices
L3 = [2, 3, 1, 4, 0]  # False:  visits all vertices but not a walk

print("Tests:")
print (LogWalk(graphA, L1))
print (LogWalk(graphA, L2))
print (LogWalk(graphA, L3))