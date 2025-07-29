from typing import List

def missing_number(nums: List[int]) -> int:
  x = 0
  for num in nums:
    x ^= num
  for i in range(len(nums) + 1):
    x ^= i
  return x