class HashMap:
  def __init__(self, size = 100) -> None:
     self.size = size
     self.buckets = [[] for _ in range(size)]
     
  def _hash(self, key):
    return hash(key) % self.size
  
  def put(self, key, value):
     index = self._hash(key)
     bucket = self.buckets[index]
     
     for i, (k, v) in enumerate(bucket):
       if key == k:
         bucket[i] = (key, value)
         return
     bucket.append((key, value))
     
  def get(self, key):
    index = self._hash(key)
    bucket = self.buckets[index]
     
    for (k, v) in bucket:
      if key == k:
        return v
    return None
  
  def delete(self, key):
    index = self._hash(key)
    bucket = self.buckets[index]
     
    for i, (k, v) in enumerate(bucket):
      if key == k:
        del bucket[i]
        return
      
  def __str__(self):
    return str([{k: v for k, v in bucket} for bucket in self.buckets if bucket])
  
hash_map = HashMap()
hash_map.put("lucas", 19)
hash_map.put("melol", 20)
hash_map.put("lionel", ("tuple", 22))

print(hash_map)
print(hash_map.get("melol"))
hash_map.delete("lionel")
print(hash_map)