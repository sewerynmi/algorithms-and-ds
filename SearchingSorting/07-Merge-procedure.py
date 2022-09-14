# Just a classic merge procedure that will merge 2 sorted lists

# runtime 0(n)  [len(A) + len(B)]
def Merge(A, B):
    MergedList = [] # init of merged (output) list
    curA = 0 # idx of first unaccommodated el. of A
    curB = 0 # idx of first unaccommodated el. of B
    for i in range(0, len(A) + len(B)):
        if curA < len(A) and curB < len(B): # pick one element from each list (A,B) until any el. left lin list
            if A[curA] <= B[curB]:
                MergedList.append(A[curA]) # Add el. from A to the MergedList (output)
                curA = curA + 1 # move to the next el. in list A for later comparison with el. from B
            else:
                MergedList.append(B[curB])
                curB = curB +1
        else:
            # if list A or B is out of values (empty)
            if curA == len(A): # el. of A have finished
                MergedList.append(B[curB]) # don't have more el.in A so add el. from B
                curB = curB +1
            else: # elements of B have finished
                MergedList.append(A[curA]) # don't have more el.in A so add el. from B
                curA = curA + 1
    return MergedList


# TEST TEST TEST
A = [1,1,2,3,5,7,8]
B = [2,3,3,5,6,7,9]
mergedList = Merge(A, B)

print(mergedList)

