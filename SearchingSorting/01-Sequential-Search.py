# Linear of sequential relationship - sorted elements in ds. like list

### Sequential Search
# Traverse list el. by el. to find el or return False in not found

def sequential_sesrch(A, itemToFind):
    for i in range(0, len(A)):
        if A[i] == itemToFind:
            return True
    return False

print('\nSequential Search')
print('1.1',sequential_sesrch([1,2,3,4], 3)) # True
print('1.1',sequential_sesrch([1,2,3,4], 5)) # False

#########################################################
