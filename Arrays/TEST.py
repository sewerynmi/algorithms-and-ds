

def SortedSquares(array):
    SortedSq = [0 for _ in array]
    for i in range(len(array)):
        SortedSq[i] = array[i] * array[i]
    SortedSq.sort()
    return SortedSq


# T3 Test
print("\nTest 3 : Sorted squares")
array1 = [1, 2, 5, 10]
print(SortedSquares(array1))
