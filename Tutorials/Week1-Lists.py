# 1. Write a function whose input is a list A. The function should return an
# index of the largest element of A.

def MaxInd(A):
    maxind=0
    for i in range (0,len(A)):
        if (A[i]>A[maxind]):
            maxind=i
    return maxind

# TEST TEST TEST
print(MaxInd([1,3,0,2,19,76,1,3])) # 5 , OK


#### rest DONE IN SECTION "LISTS" check there !!