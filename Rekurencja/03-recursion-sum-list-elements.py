# Sum of all el. of the list

def SumListElements(A, i):
    if i == 0:
        return A[0]
    auxSum = SumListElements(A, i-1)
    return auxSum + A[i]

A = [1,2,3,4]
print(SumListElements(A, len(A)-1))