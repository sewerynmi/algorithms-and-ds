# Write a function whose input is an adjacency matrix of a graph G and the output
# is the adjacency lists of G. The runtime of the function should be O(n2).

# Answer. We present a function M atrixtoList. The input of this function
# is the adjacency matrix A of a graph G and the output is the adjacency list L


# TEST TEST TEST
print("\nAdjacency Matrix to adjacency List\n")
graphA = [
    [0, 1, 0, 1],
    [1, 0, 1, 1],
    [0, 1, 0, 1],
    [1, 1, 1, 0]
]

def MatrixToList(A):
    L = []
    for i in range (0, len(A)):
        currentRowAsList = []
        for j in range(0, len(A)):
            if A[i][j] == 1:
                currentRowAsList.append(j)
        L.append(currentRowAsList)
    return L


print(MatrixToList(graphA)) 
