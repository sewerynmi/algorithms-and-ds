# 1. (a) Write a function GrowingSum(n) where n is a posititve integer number. The
# function should return a list of pairs (i, j) of integer numbers such that 0 ≤ i ≤
# n − 1, 0 ≤ j ≤ n − 1. The pairs should appear in the increasing order of the
# sum of their elements. For example, for n = 4, a legitimate output would be
# [(0, 0),(0, 1),(1, 0),(0, 2),(1, 1),(2, 0),(0, 3),
# (1, 2),(2, 1),(3, 0),(1, 3),(2, 2),(3, 1),(2, 3),(3, 2),(3, 3)].


def GrowingSum(n):
    i = 0
    myList = []
    sum = 0
    while(sum <= 2 * n - 2):
        i = 0
        while(i < n):
            j = 0
            while(j < n):
                if(i+j == sum):
                    myList.append((i, j))
                j = j + 1
            i = i + 1
        sum = sum + 1
    return myList

print(GrowingSum(4))

# 2. (a) Write a function NumSmaller(A, x) whose input is a list A of integer numbers
# and an integer number x. The function should return the number of elements
# of A that are smaller than x. The function should use a loop (not a recursion)

# (b) Solve the same question but with recursion only (no loops).

def NumSmaller(A, x):
    numOfSmaller = 0
    for i in range(0, len(A)):
        if A[i] < x:
            numOfSmaller = numOfSmaller + 1
    return numOfSmaller

def NumSmallerRec(A,x):
    if len(A) == 1:
        if A[0] < x:
            return 1
        else: 
            return 0
    elif A[0] < x:
        return 1 + NumSmaller(A[1:], x)
    else:
        return NumSmaller(A[1:], x)    

print(NumSmaller([1,2,3,4,5], 3))
print(NumSmallerRec([1,2,3,4,5], 3))