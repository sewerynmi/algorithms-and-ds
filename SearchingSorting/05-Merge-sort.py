
print('\nMERGE SORT\n')

def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr) // 2] # [0:middle]
        right_arr = arr[len(arr) // 2:] # [middle:to end of arr]
        
        # recursion bit
        merge_sort(left_arr)
        merge_sort(right_arr)
        
        # merge bit
        i = 0 # track left most el of right array (right_arr idx)
        j = 0 # tract left most el of left array (left_arr idx)
        k = 0 # merged array idx
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                k += 1
            else:
                arr[k] = right_arr[j]
                j += 1
                k += 1
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
            
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1
                
                
    
        
    
nums = [6, 3, 8, 2, 1, 9, 12, 4]
print('Unsorted:\t' , nums)
merge_sort(nums)
print('Sorted:\t\t' , nums)
print('\n')