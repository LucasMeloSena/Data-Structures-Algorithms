def containsNearbyDuplicate(nums, k):
  last_seen = {}

  for i, num in enumerate(nums):
    if num in last_seen and i - last_seen[num] <= k:
      return True
    last_seen[num] = i

  return False

result = containsNearbyDuplicate([1, 2, 3, 1, 1], 2)
print(result)