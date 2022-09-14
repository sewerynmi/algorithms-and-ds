# Sum of numb. from 0 to n

def SumNum(n):
    if n == 1:
        return 1
    auxSum = SumNum(n-1)
    return auxSum + n

print(SumNum(3))