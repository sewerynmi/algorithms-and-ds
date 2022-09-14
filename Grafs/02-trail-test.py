# Write a function whose input is an adjacency matrix A of a graph G and a list
# L # whose elements are vertices of G (possibly with repetitions). The function
# should return true if L is a trail and f alse otherwise.
# The runtime of the function should be O(len(L)).
# Hint: you may need to modify the adjacency matrix during the exploration of L.

# Answer. The first step is checking whether L is a walk using the IsW alk
# as above. I the function returns f alse then f alse can be returned immediately.
# Next, edges are tested for repetition. A straightforward way would be for
# each edge to look back and check whether it has already occurred. However,
# this approach would result in O(n2) runtime. A linear runtime requires the
# adjacency matrix modification. For instance, putting 2 instead of 1 in the entry
# of the matrix corresponding to the considered edge. A code implementating this
# idea is provided below

def isATrail(A, L):
    if IsWalk(A, L) == False:
        return False
    for i in range(1, len(L)):
        currentVertice = L[i]
        previousVertice = L[i-1]
        if A[currentVertice][previousVertice] == 2:
            return False
        # Mark as visited by changing 1 to 2. 
        A[currentVertice][previousVertice] = 2
        A[previousVertice][currentVertice] = 2
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

graphA = [
    [0, 1, 0, 1],
    [1, 0, 1, 1],
    [0, 1, 0, 1],
    [1, 1, 1, 0]
]

trailA = [0, 1, 2, 3, 1] # True, a Trail, no repeated edges
trailB = [0, 1, 2, 3, 1, 0] # False , not a Trail, repeated edge 0-1 , 1-0

print(isATrail(graphA, trailA))
print(isATrail(graphA, trailB))