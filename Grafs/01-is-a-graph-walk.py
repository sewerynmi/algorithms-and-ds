# Write a function whose input is an adjacency matrix A of a graph G and a list
# L whose elements are vertices of G (possibly with repetitions). The function
# should return true if L is a walk and f alse otherwise.
# The runtime of the function should be O(len(L)).
# Answer. A solution is pretty straightforward. Explore all vertices of the
# walk starting from the second one. For each vertex explored, check whether it is
# adjacent to the previous one. If negative return f alse immediately. Otherwise,
# return true at the end of the loop.

# Start from second vertice of the walk and check if
# visited vertrices are adjacent. If not, retun false
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

walkA = [0, 1, 2, 3, 1] # True, a Walk
walkB = [0, 1, 2, 0, 3] # False , not a Walk    

print(IsWalk(graphA, walkA)) # True
print(IsWalk(graphA, walkB)) # False