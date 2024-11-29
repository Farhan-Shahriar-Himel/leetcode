from collections import OrderedDict as Od

class LRUCache:

    def __init__(self, capacity: int):
        self.hashMap = Od()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.hashMap:
            self.hashMap.move_to_end(key)
            return self.hashMap[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self.hashMap.move_to_end(key)
        
        elif len(self.hashMap) == self.capacity:
            self.hashMap.popitem(last=False)
        
        self.hashMap[key] = value
            
    
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)