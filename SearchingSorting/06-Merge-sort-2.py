
# Helper fun. 
# Params: list, left, middle, right element
def Merge(customList, l, m, r):
    n1 = m - l + 1 # num el. in 1st sublist
    n2 = r - m # num el. in 2ns sublist
    
    L = [0] * (n1) # Temp array
    R = [0] * (n2) # Temp array
    
    # Copy elements (left)
    for i in range(0, n1):
        L[i] = customList[l + i]
    # Copy elements (right)
    for i in range(0, n2):
        R[i] = customList[m + 1 + i]
        
    i = 0 # Init idx. of 1st sublist
    j = 0 # Init idx. of 2nd sublist
    k = l # Init idx. of megred sublist
    
    #merge
    while i < n1 and j <n2:
        if L[i] <= R[j]: # if : used to merge but in sorted order, so cond.stmt. is required
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1
        k += 1
        
    # Cpy any remaining el. or R if any
    while i < n1:
        customList[k] = L[i]
        i += 1
        k += 1

    # Cpy any remaining el. or L if any        
    while i < n1:
        customList[k] = L[i]
        j += 1
        k += 1