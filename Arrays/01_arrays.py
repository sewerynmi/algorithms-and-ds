
# T1 : Find 2 num in array that sums up to the target sum and
# return them as array. Empty array if no 2 el makes sum.
def twoNumberSum(array, targetSum):
    OutputArray = []
    for i in range(0, len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == targetSum:
                OutputArray.extend([array[i], array[j]])
    return OutputArray


# T2 is array a subsequence of another array
def isValidSubsequence(array, sequence):
    if len(array) < len(sequence):
        return False
    startSearch = 0
    numsFromSequence = []
    for i in range(0, len(sequence)):
        for j in range(startSearch, len(array)):
            if sequence[i] == array[j]:
                numsFromSequence.append(array[j])
                startSearch = j + 1
    return len(sequence) == len(numsFromSequence)


# V2 O(n) time O(1) space
def isAValidSubsequenceV2(array, sequence):
    arrayIndex = 0
    sequenceIndex = 0
    while arrayIndex < len(array) and sequenceIndex < len(sequence):
        if array[arrayIndex] == sequence[sequenceIndex]:
            sequenceIndex += 1
        arrayIndex += 1
    return sequenceIndex == len(sequence)


# T3: return squares of sorted array
def SortedSquares(array):
    # Crate array with the same len as array but filled with 0's
    SortedSq = [0 for _ in array]
    for i in range(len(array)):
        SortedSq[i] = array[i] * array[i]
    SortedSq.sort()  # That sort is important here
    return SortedSq


# TEST 1
array1 = [1, 3, 4, 7, 90, 2, -9, 11]
print(twoNumberSum(array1, 97))  # [7,90]
print(twoNumberSum(array1, 32))  # []
print(twoNumberSum(array1, 2))  # [-9, 11]

# TEST 2
print("\nFind Sequence 1:")
array1 = [3, 9, 15, -2, 19, 9, 78, 13, 33]
seq1 = [3, 15, 19, 78, 33]
seq2 = [3, 15, 19, 33, 78]
seq3 = [-2]
print('t1: ', isValidSubsequence(array1, seq1))  # T
print('t2: ', isValidSubsequence(array1, seq2))  # F
print('t3: ', isValidSubsequence(array1, seq3))  # T

print('t1 v2: ', isAValidSubsequenceV2(array1, seq1))  # T
print('t2 v2 : ', isAValidSubsequenceV2(array1, seq2))  # F
print('t3 v2: ', isAValidSubsequenceV2(array1, seq3))  # T

# T3 Test
print("\nTest 3 : Sorted squares")
array1 = [1, 2, 5, 10]
print(SortedSquares(array1))
