def firstUniqChar(s: str) -> int:
  dict = {}
  for idx, char in enumerate(s):
    if (dict.get(char) is None):
      dict[char] = [idx, 1]
    else:
      dict[char][1] += 1
    
  for item in dict.values():
    if (item[1] == 1):
      return item[0]
  
result = firstUniqChar("legal")
if (result is None):
  print(-1)
else:
  print(result)