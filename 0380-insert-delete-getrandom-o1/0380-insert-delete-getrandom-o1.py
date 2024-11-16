class RandomizedSet:

    def __init__(self):
        self.d = dict()
        self.keys = []
        self.i = 0

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.d[val] = len(self.keys)
        self.keys.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.d:
            idx = self.d[val]
            lst = self.keys[-1]
            self.keys[idx] = lst
            self.keys.pop()
            self.d[lst] = idx
            del self.d[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.keys)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()