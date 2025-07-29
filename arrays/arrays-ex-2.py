def twoSum(nums, target):
  d = {}

  for i, num in enumerate(nums):
    if (target - num) in d:
      return [i, d[target - num]]
    d[num] = i

result = twoSum([2, 7, 11, 15], 9)
print(result)