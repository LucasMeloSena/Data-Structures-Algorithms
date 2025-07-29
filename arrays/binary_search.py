def binary_search(nums, n):
  l = 0
  r = len(nums) - 1
  steps = 0

  while l < r:
    steps += 1
    mid = int((l + r)/2)

    if nums[mid] == n:
      print("steps: ", steps)
      return mid
    elif nums[mid] < n:
      l = mid + 1
    else:
      r = mid + 1
  return -1

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
binary_search(b, 3)