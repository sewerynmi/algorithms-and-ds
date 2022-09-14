# Check if array contain any duplicate number

# Time O(n) Space: 0(n)
def checkIfHaveDuplicate(array):
    checkoutNums = set()
    for num in array:
        if num in checkoutNums:
            return True
        checkoutNums.add(num)
    return False

# Tests
nums = [1, 2 ,3, 4, 1]
print("\nTest 1 have duplicate : " , checkIfHaveDuplicate(nums)) # True

nums = [1, 2 ,3, 4, 5]
print("\nTest 2 have duplicate : " , checkIfHaveDuplicate(nums)) # False

nums = [1, 2 ,3, 4, 5, 6, 7, 8, 8]
print("\nTest 3 have duplicate : " , checkIfHaveDuplicate(nums)) # True
