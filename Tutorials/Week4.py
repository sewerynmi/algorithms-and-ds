# 3. Write a function whose input is a list A of integers. The function should
# return T rue if any two elements in the list differ by at most 20 and F alse
# otherwise. The runtime of the function should be O(n).

# Answer. The largest difference of two elements of A is the difference
# between the largest and the smallest elements of A. So, all what we need
# to compute max(A) and min(A) (both can be done in a linear time).
# Then if max(A) − min(A) ≤ 20, the prorgram should return T rue and
# F alse otherwise.

print('\nTEST task 3')
def isDiff20(A):
    return (max(A) - min(A)) <= 20 

# TESTS Task 3
print('3.1',isDiff20([1,2,3,4,5])) # True
print('3.2',isDiff20([2,17,3,1,23,7,11])) # False



# 4. Let A and B be two lists of integers without repetitions so that A contains
# all the elements of B but one. Write a function whose input are A and B.
# The function should return the element missing in A. The runtime of the
# function should be O(n).

# Answer. sum(B) is the sum of all the elements of A plus the missing
# element. Therefore, to identify the missing element we just compute
# sum(B) − sum(A) and return the resulting number.

def findMissingEl(A,B):
    sumA = sum(A)
    sumB = sum(B)
    return sumB - sumA

print('\nTEST task 4')
print(findMissingEl([1,2,3],[1,2,3,4]))