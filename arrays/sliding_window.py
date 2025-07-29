def maximum_length_substring(array) -> int:
  l, r = 0, 0
  _max = 1
  counter = {}
  counter[array[0]] = 1

  while (r < len(array) - 1):
    r += 1
    if counter.get(array[r]):
      counter[array[r]] += 1
    else:
      counter[array[r]] = 1

    while counter[array[r]] == 2:
      counter[array[l]] -= 1
      l += 1

  _max = max(_max, r-l+1)
  return _max

a = ["b", "b", "c", "a", "a", "a", "b"]
result = maximum_length_substring(a)
print(result)