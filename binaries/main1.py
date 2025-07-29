def number_of_steps(num: int) -> int:
  steps = 0
  while num > 0:
    if num & 1:
      num -= 1
    else:
      num >>= 1
    steps += 1
  
  return steps

print(number_of_steps(14))