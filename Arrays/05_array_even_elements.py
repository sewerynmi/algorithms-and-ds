
# Find all even elements
def EvenElements(A):
    EvenOnes = []
    for num in A:
        if num % 2 == 0:
            EvenOnes.append(num)
    return EvenOnes

print("\nTESTS\n")

print(EvenElements([1,2,3,4,5,6,7,8,9,10])) # [2, 4, 6, 8, 10]
print(EvenElements([1,3,5,7,9,11])) # []