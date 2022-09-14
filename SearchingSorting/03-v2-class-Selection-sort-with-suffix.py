
def SelectionSort(A):
    for i in range(0, len(A)):
        minIdx = MinSuffix(A, i) # find idx of the smallest value
        A[i], A[minIdx] = A[minIdx], A[i] # swap items

# Helper Min Suffix to find idx of the min el. in the range
def MinSuffix(A, i):
    minIdx = i
    for j in range(i + 1, len(A)):
        if A[j] < A[minIdx]:
            minIdx = j
    return minIdx


# TEST TEST TES
print("\nTest helper MinSuffix only\n")
print(MinSuffix([0,3,6,12,7,1,5], 3)) # 5 as idx of 1 is 5

print("\nSELECTION SORT from the BBK session\n")
A = [0,3,6,12,7,1,5]
print("Original: \t", A)
SelectionSort(A)
print("Sorted: \t" , A)
