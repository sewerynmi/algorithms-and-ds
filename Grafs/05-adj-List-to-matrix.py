# Write a function is input is adjacency lists L The function should return an
# adjacency matrix A of G. The runtime of the function should be O(n2).
# Answer. The solution is in a form of a function ListtoM atrix(L) where L
# is the adjaency list. The output is the adjacency matrix.

def ListToMatrix(L):
    M = []
    for i in range(0, len(L)):
        matrixRow = [0] * len(L)
        for j in range(0, len(L[i])):
            matrixRow[L[i][j]] = 1
        M.append(matrixRow)
    return M

# TEST TEST TEST
print("\nAdjacency List to adjacency Matrix\n")
graphA = [
    [1, 3], 
    [0, 2, 3], 
    [1, 3], 
    [0, 1, 2]
]

print(ListToMatrix(graphA)) 
