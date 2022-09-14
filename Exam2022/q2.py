
def LessThan100(A):
    for i in range(len(A) - 1, 0, -1):
        if (A[i] - A[i - 1] < 100):
            return True;
    return False;

print("1")
print(LessThan100([1,2,3,100]))
print(LessThan100([1,2,3,1020]))
print(LessThan100([1,110,290,700]))
print(LessThan100([-20,3,110,290,700]))


def LessThan1002(A):
    prev = A[0]
    size = len(A)
    for i in range(1,size):
        cur = A[i]
        if (abs(cur-prev) < 100):
            #print (prev, cur)
            return True
        prev = cur
    return False

def LessThan1003(A):
    prev = A[0]
    size = len(A)
    for i in range(1,size):
        cur = A[i]
        if (abs(cur-prev) < 100):
            #print (prev, cur)
            return True
        prev = cur
    return False


print("2")
print(LessThan1002([1,2,3,100]))
print(LessThan1002([1,2,3,1020]))
print(LessThan1002([1,110,290,700]))

print("3")
print(LessThan1003([1,2,3,100]))
print(LessThan1003([1,2,3,1020]))
print(LessThan1003([1,110,290,700]))
