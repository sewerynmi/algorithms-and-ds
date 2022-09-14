# 1. Write a function MaxAvColumn(A) whose input is a matrix A. The
# function should return the largest average of a column. Feel free to use
# functions sum and max
# Answer. We calculate averages for each column, put the averages to a
# list and compute the maximum of the list.


def MaxAvColumn(A):
    n = len(A[0]) # num of columns
    Averages = []
    for i in range(0, n):
        CurCol = getColumn(A, i)
        Averages.append(sum(CurCol) / len(CurCol))
    return max(Averages)
        
        

# Helpers
# T1 get matrice column.
def getColumn(A, j):
    Column = []
    for i in range (0, len(A)):
        Column.append(A[i][j])
    return Column

# TEST TEST TEST
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [1, 2, 1],
    [3, 1, 1],
    [2, 5, 3]
]

print("\nTask 1: ")
print("1:" , MaxAvColumn(matrix1))
print("2:" , MaxAvColumn(matrix2))


################################### TASK 2 #######################################

# Write a function AllIndices whose input is a list A. For convenience, let
# us denote the length of A by n. The function should return T rue if A
# contains all the numbers 0 to n − 1 and each number occurs exactly once.
# Otherwise, the function shuld return F alse

# Answer. We introduce a new list Indices of length n. Initially the list
# contains all zeroes. The program fills the list so that Indices[i] contains
# the number of times i occurs as an element of A. In the end it only remains
# to check whether all the elements of Indices equal 1.
# LIST TASK ???
def AllIndices(A):
    n=len(A)
    Indices=[0] * n
    for i in range (0,n):
        curel=A[i]
        if curel < 0 or curel > n-1: # check if each el. in list i in range od index 0 to n-1
            return False
        Indices[curel] = Indices[curel] + 1
    for i in range (0,n):
        if Indices[i] != 1:
            return False
    return True

print("\nTask 2:")
print(AllIndices([0,1,2,3])) # T
print(AllIndices([0,1,2,4])) # F



################################### TASK 3 #######################################

# A Latin square is an n×n matrix where each row and each column contains
# numbers 0 to n−1 and each number occurs exactly once. Write a function
# IsLatinSquare whose input is a square matrix A of integers. The function
# should return T rue if A is a Latin square and F alse otherwise. 
# Hint: use the function AllIndices as in the previous question. Answer.
# Example: col and row must have unique values
# [A, B, C]
# [B, C, A]
# [C, A, B]

def IsLatinSquare(A):
    for i in range(0, len(A)):
        if not AllIndices(A[i]):
            return False
        if not AllIndices(getColumn(A, i)):
            return False
    return True


# TEST TEST TEST
matrixLatin1 = [
    [0, 1, 2],
    [1, 2, 0],
    [2, 0, 1]
] # T

matrixLatin2 = [
    [0, 2, 1],
    [1, 2, 0],
    [2, 0, 1]
] # F

print("\nTask 3: Latin suqre matrix")
print("1: ", IsLatinSquare(matrixLatin1))
print("2: ", IsLatinSquare(matrixLatin2))


################################### TASK 4 #######################################

# In this question we will consider the table Distances as in Week 2 slides.
# Let S be a list of cities (that is, elements of S are 0, . . . , len(Distances)−1). 
# Cities can occur more than once in S. Imagine a person starting at S[0]
# then moving to S[1] then to S[2] and so on until s/he reaches S[len(S)−1].
# The total distance covered by the person is the distance between S[0] and
# S[1] plus the distance between S[1] and S[2] and so on. Write a function
# JourneyLength(A, S) that returns the distance covered by the person.

# S - cities
def JourneyLength(Distances, S):
    TotalDistance = 0
    for i in range(0, len(S) - 1):
        curCity = S[i]
        nextCity = S[i +1]
        TotalDistance = TotalDistance + Distances[curCity][nextCity]
    return TotalDistance

Distances = [
    [0, 2, 5, 9],
    [2, 0, 10, 11],
    [5, 10, 0, 13],
    [9, 11, 13, 0]
]
Cities = ['London', 'Leeds', 'Birmingham', 'Glasgow']

print("\nTask 4 : city distances\n")
print("1: ", JourneyLength(Distances, [0,1]))
print("1: ", JourneyLength(Distances, [0,1,2,3]))


################################### TASK 5 #######################################

# In this problem we continue to work with Distances matrix. Let us say
# that two cities are close to each other if the distance between them is at
# most 10 miles. Write a program CloseCities(Distances) that returns the
# number of pairs of cities close to each other. Make sure that the pairs of
# a city with itself do not count and each pair of cities is counted only once.

def ClosestCities(Distances):
    n = len(Distances)
    TotalCloses = 0
    for i in range(0, n - 1):
        for j in range(i+1, n):
            if Distances[i][j] <= 10:
                TotalCloses = TotalCloses + 1
    return TotalCloses

print("\Task 5: Total closes cities\n")
print("1: ", ClosestCities(Distances))

############## MAtrices Fiddle ###############

# Fiddle1 : Check if each column contains at least one Even numer and retur True, otwewise: False

def EachColumnHasEven(A):
    for i in range(0, len(A)):
        if ExistEvenInList(getColumn(A, i)) == False:
            return False
    return True

def ExistEvenInList(A):
    for i in range(0, len(A)):
        if A[i] % 2 == 0:
            return True
    return False

print("\nJust test if list has any even number\n")
print("1. has even [True] : " , ExistEvenInList([1,3,5,8,9])) 
print("2. has even [False]: " , ExistEvenInList([1,3,11,13,9]))

print("\nTest if each col has Even value\n")
matrix1= [
    [1,2,3],
    [2,1,3],
    [3,1,2]
] # T

matrix2= [
    [1,2,3],
    [3,1,2],
    [3,1,2]
] # F
print("1. all cols has even [True] : " , EachColumnHasEven(matrix1)) # T
print("2. all cols has even [False]: " , EachColumnHasEven(matrix2)) # F