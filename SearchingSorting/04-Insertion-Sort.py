
print('\nINSERTION SORT\n')

def insertion_sort(list_a):
    for i in range(1, len(list_a)):
        value_to_sort = list_a[i]
        while list_a[i-1] > value_to_sort and i > 0: # i > 0 because we don't want to start checking the negative indexes of list_a
            list_a[i], list_a[i-1] =  list_a[i-1],  list_a[i]
            i = i - 1
    return list_a
                
                
    
        
    
nums = [6, 3, 8, 2, 1, 9, 12, 4]
print('Unsorted:\t' , nums)
insertion_sort(nums)
print('Sorted:\t\t' , nums)
print('\n')