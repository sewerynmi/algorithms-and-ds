
# T1 get matrice column.
def getColumn(A, j):
    Column = []
    for i in range (0, len(A)):
        Column.append(A[i][j])
    return Column

# T2: Return true if each column contains EVEN numbers
def EachColumnEvenNums(A):
    for i in range(0, len(A)):
        CurrColumn = getColumn(A,i)
        for n in CurrColumn:
            if n % 2 != 0:
                return False
    return True

# Test T1
m1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
m2 = [
    [2, 4, 6],
    [8, 10, 12],
    [14, 16, 18]
]

print("\nTask 1: get matric column :")
print(getColumn(m1, 1)) # [2,5,8]

print("\nTask 2: Only even num in columns ? :")
print(EachColumnEvenNums(m1)) # F
print(EachColumnEvenNums(m2)) # T