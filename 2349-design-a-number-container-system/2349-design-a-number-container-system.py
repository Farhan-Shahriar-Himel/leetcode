class NumberContainers:

    def __init__(self):
        self.mp = defaultdict(SortedSet)
        self.index_mp = defaultdict(int)
        
    def change(self, index: int, number: int) -> None:
        if index in self.index_mp:
            num = self.index_mp[index]
            self.mp[num].remove(index)
        self.index_mp[index] = number
        self.mp[number].add(index)

    def find(self, number: int) -> int:
        if len(self.mp[number]) != 0:
            return next(iter(self.mp[number]))
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)