# Optimal Solution

class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.buildHeap(array)

    # O(n) Time |  O(1) Space
    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
        for currentIdx in reversed(range(firstParentIdx + 1)):
            self.siftDown(currentIdx, len(array) - 1, array)
        return array

    # O(logn) time | O(1) Space
    def siftDown(self, currentIdx, endIdx, heap):
        leftIdx = currentIdx * 2 + 1
        while leftIdx <= endIdx:
            rightIdx = currentIdx * 2 + 2 if currentIdx * 2 + 2 <= endIdx else -1
            if rightIdx != -1 and heap[rightIdx] < heap[leftIdx]:
                idxToSwap = rightIdx
            else:
                idxToSwap = leftIdx

            if heap[idxToSwap] < heap[currentIdx]:
                self.swap(currentIdx, idxToSwap, heap)
                currentIdx = idxToSwap
                leftIdx = currentIdx * 2 + 1
            else:
                break

    # O(logn) time | O(1) Space
    def siftUp(self, currentIdx, heap):
        parentIdx = (currentIdx - 1) // 2
        while currentIdx > 0 and heap[currentIdx] < heap[parentIdx]:
            self.swap(currentIdx, parentIdx, heap)
            currentIdx = parentIdx
            parentIdx = (currentIdx - 1) // 2

    def peek(self):
        return self.heap[0]

    # O(logn) time | O(1) Space
    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        valueToRemove = self.heap.pop()
        self.siftDown(0, len(self.heap) - 1, self.heap)
        return valueToRemove

    # O(logn) time | O(1) Space
    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap) - 1, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]
