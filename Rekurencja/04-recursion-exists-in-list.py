# Check if value exists in the list

from operator import truediv

# x - search value
# i - idx of list ( usually last (max) elemet as recursion is going to idx=0 : len(A)-1 )
def ExistRecustion(A, x, i):
    if A[i] == x:
        return True
    if i == 0:
        return False
    return ExistRecustion(A, x, i-1)

A = [1,7,9,2,12,89]
print(ExistRecustion(A, 12, len(A)-1))