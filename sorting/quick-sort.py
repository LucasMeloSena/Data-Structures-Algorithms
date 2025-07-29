# not in-place
def quick_sort_not_inplace(arr):
  if (len(arr) <= 1):
    return arr
  
  size = len(arr)
  pivot = arr[size-1]
  
  left = []
  right = []
  equal = []
  
  for x in arr: 
    if (x < pivot):
      left.append(x)
    elif (x > pivot):
      right.append(x)
    else:
      equal.append(x)
      
  return quick_sort_not_inplace(left) + equal + quick_sort_not_inplace(right)

def quick_sort_in_place(arr, left, right):
  if left < right:
    pivot = partition(arr, left, right)
    quick_sort_in_place(arr, left, pivot - 1)
    quick_sort_in_place(arr, pivot + 1, right)
    
  return arr
    
def partition(arr, left, right):
  pivot = arr[right]
  i = left - 1
  
  for j in range(left, right):
    if (arr[j] < pivot):
      i += 1
      arr[i], arr[j] = arr[j], arr[i]
    
  arr[i+1], arr[right] = arr[right], arr[i+1]
  return i + 1

list_example = [3, 2, 6, 4, 8, 3]
sorted_list1 = quick_sort_in_place(list_example, 0, len(list_example)-1)
print(sorted_list1)