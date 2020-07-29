# Andre Doumad

import unittest, random
# MaxHeap
class MaxHeap(object):
    # heap
    def __init__(self):
        self.heap = []

    # get parent index
    def getParent(self, i):
        return int((i-1)/2)
    # get left index
    def getLeft(self, i):
        return 2*i+1
    # get right index
    def getRight(self, i):
        return 2*i+2

    # has parent
    def hasParent(self, i):
        return self.getParent(i)>=0
    # has left
    def hasLeft(self, i):
        return self.getLeft(i)<len(self.heap)
    # has right
    def hasRight(self, i):
        return self.getRight(i)<len(self.heap)

    # heapifyUp
    def heapifyUp(self, i):
        while self.hasParent(i) and self.heap[self.getParent(i)] < self.heap[i]:
            self.swap(i, self.getParent(i))
            i = self.getParent(i)

    # heapifyDown
    def heapifyDown(self, i):
        while self.hasLeft(i):
            max_child_index = self.getMaxChildIndex(i)
            if max_child_index == -1:
                break
            if self.heap[max_child_index] > self.heap[i]:
                self.swap(i, max_child_index)
                i = max_child_index
            else:
                break

    # getMaxChildIndex
    def getMaxChildIndex(self, i):
        if self.hasLeft(i):
            left_index = self.getLeft(i)
            if self.hasRight(i):
                right_index = self.getRight(i)
                if self.heap[left_index] >= self.heap[right_index]:
                    return left_index
                else:
                    return right_index
            else:
                return -1
        else:
            return -1

    # swap
    def swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    # popMax
    def popMax(self):
        if len(self.heap) == 0:
            return -1
        root = 0
        last_index = len(self.heap)-1
        self.swap(0, last_index)
        root = self.heap.pop()
        self.heapifyDown(0)
        return root

    # push
    def push(self, key):
        if len(self.heap) ==0:
            self.heap.append(key)
            return
        self.heap.append(key)
        self.heapifyUp(len(self.heap)-1)

    # peek
    def peek(self):
        if len(self.heap)==0:
            return None
        else:
            self.heapifyDown(0)
            return self.heap[0]
    
    def printHeap(self):
        print(str(self.heap))

# unittest
class unitTest(unittest.TestCase):
    def test_0(self):
        heap = MaxHeap()
        for i in range(0, 15):
            heap.push(random.randrange(0,150))
        
        maxValue = 0
        while maxValue != -1:
            print('')
            heap.printHeap()
            maxValue = heap.popMax()
            print(str(maxValue))

if __name__ == "__main__":
    unittest.main()

'''
OUTPUT:

[144, 140, 139, 75, 78, 122, 116, 30, 52, 30, 23, 20, 75, 81, 60]
144

[140, 78, 139, 75, 60, 122, 116, 30, 52, 30, 23, 20, 75, 81]
140

[139, 78, 122, 75, 60, 81, 116, 30, 52, 30, 23, 20, 75]
139

[122, 78, 116, 75, 60, 81, 75, 30, 52, 30, 23, 20]
122

[116, 78, 81, 75, 60, 20, 75, 30, 52, 30, 23]
116

[81, 78, 75, 75, 60, 20, 23, 30, 52, 30]
81

[78, 75, 75, 52, 60, 20, 23, 30, 30]
78

[75, 60, 75, 52, 30, 20, 23, 30]
75

[75, 60, 30, 52, 30, 20, 23]
75

[60, 52, 30, 23, 30, 20]
60

[52, 30, 30, 23, 20]
52

[30, 20, 30, 23]
30

[30, 20, 23]
30

[23, 20]
23

[20]
20

[]
-1
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK

'''
