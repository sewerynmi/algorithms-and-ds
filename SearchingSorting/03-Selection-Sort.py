
print('\nSELECTION SORT\n')
def selection_sort(list_a):
    indexing_length = range(0, len(list_a) - 1) # -1 as if we have 1 item left it mean list is sorted
    for i in indexing_length:
        min_value = i
        for j in range(i+1, len(list_a)):
            if list_a[j] < list_a[min_value]:
                min_value = j
        if min_value != i:
            # Swap values now
            list_a[min_value], list_a[i] = list_a[i], list_a[min_value]
    return list_a
                
                
    
        
    
nums = [6,3,8,2,1,9,12,4]
print('Unsorted:\t' , nums)
selection_sort(nums)
print('Sorted:\t\t' , nums)
print('\n')