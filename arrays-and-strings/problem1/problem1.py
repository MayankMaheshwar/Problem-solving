"""
Given an array of numbers, replace each even number with two of the same number. e.g, [1,2,5,6,8] -> [1,2,2,5,6,6,8,8]. Assume that the array has enough space to accommodate the result.
"""

def countEven(arr):
    count = 0
    for i in arr:
        if i%2==0:
            count += 1
    return count

def duplicateEven(arr):
    arr_end_idx = len(arr)-1
    even_count = countEven(arr)
    arr.extend([None]*even_count)
    end = len(arr)-1
    while arr_end_idx >= 0:
        if arr[arr_end_idx] %2 == 0:
            arr[end],arr[end-1] = arr[arr_end_idx],arr[arr_end_idx]
            end -= 2
        else:
            arr[end] = arr[arr_end_idx]
            end -=1
        arr_end_idx -= 1
    return arr

print([1,2,2,5,6,6,8,8])
print(duplicateEven([1,2,5,6,8]))
