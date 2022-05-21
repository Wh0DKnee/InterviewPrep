

def parent(index):
    return index // 2


def left(index):
    return index * 2 + 1


def right(index):
    return index * 2 + 2


class MinHeap:

    def __init__(self):
        self.heap = []

    def add(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)

    def extract_min(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        minimum = self.heap.pop()
        self.heapify_down(0)
        return minimum

    def heapify_down(self, index):
        l, r = left(index), right(index)
        if l >= len(self.heap) and r >= len(self.heap):
            return

        if l >= len(self.heap):
            smaller = r
        elif r >= len(self.heap):
            smaller = l
        else:
            smaller = l if self.heap[l] < self.heap[r] else r

        if self.heap[smaller] < self.heap[index]:
            self.heap[smaller], self.heap[index] = self.heap[index], self.heap[smaller]

    def heapify_up(self, index):
        if index == 0:
            return
        if self.heap[parent(index)] > self.heap[index]:
            self.heap[index], self.heap[parent(index)] = self.heap[parent(index)], self.heap[index]
            self.heapify_up(parent(index))

    def peek(self):
        return self.heap[0]


heap = MinHeap()
heap.add(10)
heap.add(4)
heap.add(15)
print(heap.extract_min())
heap.add(20)
heap.add(0)
heap.add(30)
print(heap.extract_min())
print(heap.extract_min())
heap.add(2)
heap.add(5)
heap.add(-1)
heap.add(-1)
print(heap.heap)


