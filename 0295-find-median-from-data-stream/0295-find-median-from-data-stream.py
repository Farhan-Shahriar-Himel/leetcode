from heapq import heappush as push, heappop as pop

class MedianFinder:
    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if not self.left:
            push(self.left, -num)
        if not self.right:
            push(self.right, num)
        
        if self.left > self.right:
            top = -pop(self.left)
            if top > num:
                top, num = num, top
            push(self.left, -top)
            push(self.right, num)
        
        else:
            top = pop(self.right)
            if top > num:
                top, num = num, top
            push(self.left, -top)
            push(self.right, num)

    def findMedian(self) -> float:
        # print(sorted(self.left), sorted(self.right))
        if (len(self.left) + len(self.right)) % 2 == 1:
            med = -pop(self.left)
            push(self.left, -med)
            return med
        
        med1 = -pop(self.left)
        med2 = pop(self.right)
        push(self.left, -med1)
        push(self.right, med2)
        return (med1 + med2) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()