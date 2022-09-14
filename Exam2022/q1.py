


def GrowingSum(A):
    B = [0] * len(A)
    B[0] = A[0]
    for i in range(1, len(A)):
        B[i] = B[i-1] + A[i]
    return B

print(GrowingSum([1,2,3,-1]))