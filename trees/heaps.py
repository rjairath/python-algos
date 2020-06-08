class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)

    def percDown(self, i):
        while (2*i <= self.currentSize):
            # returns the index
            minChild = self.findMinChild(i)
            if minChild < self.heapList[i]:
                self.heapList[i], self.heapList[minChild] = self.heapList[minChild], self.heapList[i]

            i = minChild

    def findMinChild(self, i):
        if 2*i + 1 > self.currentSize:
            return 2*i
        else:
            if self.heapList[2*i] < self.heapList[2*i + 1]:
                return 2*i
            else:
                return 2*i + 1

    def deleteMin(self):
        removed = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.heapList.pop()
        self.currentSize -= 1
        self.percDown(1)
        return removed

    def buildHeap(self, listSample):
        self.currentSize = len(listSample)
        self.heapList = [0] + listSample

        i = self.currentSize // 2
        while(i > 0):
            self.percDown(i)
            i = i-1

arr = [9, 6, 5, 2, 3]
root = BinHeap()
root.buildHeap(arr)

x = root.deleteMin()
print(x)
