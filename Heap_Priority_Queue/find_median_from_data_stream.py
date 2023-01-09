import heapq


class MedianFinder:

    def __init__(self):
        self.maxHeap, self.minHeap = [], []

    def addNum(self, num: int) -> None:
        if len(self.maxHeap) == len(self.minHeap):
            if len(self.maxHeap) == 0 or num <= -self.maxHeap[0]:
                heapq.heappush(self.maxHeap, -num)
            else:
                heapq.heappush(self.minHeap, num)
        elif len(self.maxHeap) > len(self.minHeap):
            if num < -self.maxHeap[0]:
                heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))
                heapq.heappush(self.maxHeap, -num)
            else:
                heapq.heappush(self.minHeap, num)
        else:
            if num > self.minHeap[0]:
                heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
                heapq.heappush(self.minHeap, num)
            else:
                heapq.heappush(self.maxHeap, -num)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] + (-self.maxHeap[0])) / 2
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        return -self.maxHeap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
