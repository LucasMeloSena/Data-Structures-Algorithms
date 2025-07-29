def binary_search(nums, n, l, r):
  while l <= r:
    mid = int((l + r)/2)

    if nums[mid] == n:
      return mid
    elif nums[mid] < n:
      l = mid + 1
    else:
      r = mid - 1
  return -1

def exponential_search(nums, target):
  if nums[0] == target:
    return 0

  n = len(nums)
  i = 1

  while i < n and nums[i] < target:
    i *= 2

  left = i // 2
  right = min(i, n - 1)

  res = binary_search(nums, target, left, right)
    
  if res == -1:
    return -1
  return res

array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
goal = 19
result = exponential_search(array, goal)
print(result)