def HowMany(A, x):
    n = len(A)
    leftIndex = leftPart(A, x, 0, n)
    rightIndex = rightPart(A, x, leftIndex, n)  
    return rightIndex - leftIndex

def leftPart(array, target, lowestIdx, highestIdx):
    while lowestIdx < highestIdx:
        mid = (lowestIdx + highestIdx) // 2
        if array[mid] < target: lowestIdx = mid+1
        else: highestIdx = mid
    return lowestIdx

def rightPart(array, target, lowetIndex, highestIndex):
    while lowetIndex < highestIndex:
        mid = (lowetIndex+highestIndex)//2
        if target < array[mid]: highestIndex = mid
        else: lowetIndex = mid+1
    return lowetIndex

A = [1,2,4,4,4,5,15]
target = 4
print(HowMany(A, target))