import unittest

# quicksort
class QuickSort(object):

    # sort
    def sort(self, n):
        self.quickSort(n, 0, len(n)-1)
        return n

    # recursive sort
    def quickSort(self, n, left, right):
        # if left is larger than right - return
        if left >= right:
            return
        # pivot
        pivot = n[(left+right)//2]
        # partition
        index = self.partition(n, left, right, pivot)
        # sort left
        self.quickSort(n, left, index-1)
        # sort right
        self.quickSort(n, index, right)

    # partition
    def partition(self, n, left, right, pivot):
        # while left is less than or equal to right
        while left <= right:
            # walk left towards pivot
            while n[left] < pivot:
                left+=1
            # walk right towards pivot
            while n[right] > pivot:
                right-=1
            # swap if right is greater or equal to left
            if left <= right:
                #swap
                self.swap(n, left, right)
                left+=1
                right-=1
        return left

    # swap
    def swap(self, n, left, right):
        temp = n[left]
        n[left] = n[right]
        n[right] = temp

# unittest
class uniTest(unittest.TestCase):

    def test_a(self):
        qsort = QuickSort()
        result = qsort.sort([7,10,5,0,4,6,8,1,3,9,2])
        print('result ',result)
        self.assertEqual(result,[0,1,2,3,4,5,6,7,8,9,10], ' should array sorted 0-10 ' )

if __name__ == "__main__":
    unittest.main()