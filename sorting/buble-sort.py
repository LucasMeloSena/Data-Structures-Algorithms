def bubble(nums):
  size = len(nums)
  for _ in nums:
    is_sorted = True
    for i in range(size-1):
      if (nums[i] > nums[i+1]):
        is_sorted = False
        lowest_value = nums[i+1]
        nums[i+1] = nums[i]
        nums[i] = lowest_value
        
    if (is_sorted):
      return nums 
  return nums

result = bubble([1,2,5,4,3])
print(result)