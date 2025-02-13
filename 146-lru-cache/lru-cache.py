from collections import deque

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.limit = capacity
        self.deque = deque()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            self.deque.remove(key)
            self.deque.append(key)
            return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.deque.remove(key)
            self.cache[key] = value
            self.deque.append(key)
        else:
            self.cache[key] = value
            self.deque.append(key)
        
        if len(self.cache) > self.limit:
            oldest_key = self.deque.popleft() 
            del self.cache[oldest_key]       
# Example usage:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key, value)
