

def MaxIndexRec(A,i):
    if i == 0:
        return 0
    j = MaxIndexRec(A, i-1)
    if A[j] < A[i]:
        return i
    return j

A = [1,3,7,8,12,6,10]
print(MaxIndexRec(A, len(A)-1))