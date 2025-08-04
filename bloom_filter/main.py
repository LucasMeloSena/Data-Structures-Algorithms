import hashlib

class BloomFilter:
  def __init__(self, size=100, hash_count=3):
    self.bloom_filter = [0] * size
    self.size = size
    self.hash_count = hash_count
    
  def _hashes(self, value):
    hashes = []
    for i in range(self.hash_count):
      hash_digest = hashlib.sha256((value + str(i)).encode()).hexdigest()
      hash_int = int(hash_digest, 16)
      hashes.append(hash_int % self.size)
    return hashes
  
  def put(self, value):
    for index in self._hashes(value):
      self.bloom_filter[index] = 1

  def search(self, value):
    return all(self.bloom_filter[index] == 1 for index in self._hashes(value))
    
bloom_filter = BloomFilter()
bloom_filter.put("lucas")
bloom_filter.put("melol")
bloom_filter.put("lionel")

print(bloom_filter.search("joao"))
print(bloom_filter.search("lucas"))
print(bloom_filter.search("melol"))
print(bloom_filter.search("lionel"))