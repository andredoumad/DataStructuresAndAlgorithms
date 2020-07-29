# Andre Doumad

import unittest, os, sys


import numpy
import inspect

class DynamicArray():

    def __init__(self, capacity):
        self.size = 0
        self.data = numpy.empty(capacity, dtype=object)
        self.capacity = capacity
        print('initialized dynamic array.')
        print('data size: ' + str(self.data.size))
        print('size: ' + str(self.size))
        print('capacity: ' + str(self.capacity))

    def Hello(self):
        hello = "hello"
        return hello

    def array_get(self, index):
        return self.data[index]

    def array_set(self, index, value):
        while index >= self.capacity:
            self.resize()
        self.data[index] = value
        self.size = index
        self.PrintArray()

    def add(self, value):
        self.PrintArray()
        if self.size >= self.capacity:
            self.resize()
        self.data[self.size] = value
        self.size += 1
        self.PrintArray()

    def insert(self, index, value):
        self.PrintArray()
        if index >= self.capacity:
            self.resize()

        for i in reversed(range(index, self.size)):
            self.data[i+1] = self.data[i]
            self.PrintArray()
        self.data[index] = value
        self.size += 1
        self.PrintArray()

    def resize(self):
        print('resizing!')
        temp_data = numpy.empty(self.capacity*2, dtype=object)

        for i in range(0, self.size):
            temp_data[i] = self.data[i]

        del self.data 
        self.data = temp_data
        self.capacity = self.capacity*2

    def delete(self, index):
        self.PrintArray()
        for i in range(index, self.size):
            if int(i+1) < self.size:
                self.data[i] = self.data[i+1]
            else:
                self.data[i] = None

        self.size -= 1
        self.PrintArray()

    def array_size(self):
        print('size is: ' + str(self.size))
        return int(self.size)

    def PrintArray(self):
        print('capacity is: ' + str(self.capacity))
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 2)
        print('printing method:', calframe[1][3])
        for i in range(0, self.capacity):
            print('index: ' + str(i) + ' val: ' + str(self.data[i]))
        print('size is: ' + str(self.size))
        print('capacity is: ' + str(self.capacity))

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False 

    def array_contains(self, value):
        print('array_contains...')
        print('value to search for is: ' + str(value))
        found = False
        searching = True
        while searching:
            for i in range(0, self.size):
                if self.data[i].find(value) != -1:
                    found = True
                    searching = False
            searching = False
        return found




class TestDynamicArray(unittest.TestCase):

    def test_init(self):
        self.darray = DynamicArray(2)
        self.assertEqual(self.darray.capacity, 2, 'should equal 2')

    def test_Hello(self):
        self.darray = DynamicArray(2)
        self.assertEqual(self.darray.Hello(), "hello", "should return hello as string")

    def test_GetAndSet(self):
        print('get and set...')
        self.darray = DynamicArray(2)
        self.darray.array_set(42, "a")
        self.assertEqual(self.darray.array_get(42), "a", "element 0 of array should equal a")


    def test_insert(self):
        self.darray = DynamicArray(2)
        self.darray.add('a')
        self.darray.add('b')
        self.darray.add('c')

        self.darray.insert(1, "d")
        # self.darray.array_size()
        self.assertEqual(self.darray.array_size(), 4, 'array size should be 4')
        self.assertEqual(self.darray.data[0], 'a', 'first element should be a')
        self.assertEqual(self.darray.data[1], 'd', 'second element should be d')
        self.assertEqual(self.darray.data[2], 'b', 'third element should be b')
        self.assertEqual(self.darray.data[3], 'c', 'fourth element should be c')

    def test_DeleteFirst(self):
        self.darray = DynamicArray(2)
        self.darray.add("a")
        self.darray.add("b")
        self.darray.add("c")
        self.darray.delete(0)

        self.assertEqual(self.darray.array_size(), 2, 'size should equal 2')
        self.assertEqual(self.darray.array_get(0), "b", 'index 0 should equal b')
        self.assertEqual(self.darray.array_get(1), "c", 'index 1 should equal c')
        self.assertEqual(self.darray.array_get(2), None, 'index 2 should equal nothing')

    def test_deleteMiddle(self):
        self.darray = DynamicArray(2)
        print('testing delete middle')
        self.darray.add("a")
        self.darray.add("b")
        self.darray.add("c")
        self.darray.delete(1)

        self.assertEqual(self.darray.array_size(), 2, 'size should equal 2')
        self.assertEqual(self.darray.array_get(0), "a", 'index 0 should equal a')
        self.assertEqual(self.darray.array_get(1), "c", 'index 1 should equal b')
        self.assertEqual(self.darray.array_get(2), None, 'index 2 should equal none')

    def test_deleteLast(self):
        print('testing delete last')
        self.darray = DynamicArray(2)
        self.darray.add("a")
        self.darray.add("b")
        self.darray.add("c")
        self.darray.delete(2)

        self.assertEqual(self.darray.array_size(), 2, 'size should equal 2')
        self.assertEqual(self.darray.array_get(0), "a", 'index 0 should equal a')
        self.assertEqual(self.darray.array_get(1), "b", 'index 1 should equal b')
        self.assertEqual(self.darray.array_get(2), None, 'index 2 should equal none')

    def test_isEmpty(self):
        self.darray = DynamicArray(2)
        self.assertTrue(self.darray.isEmpty(), " array isEmpty should return true")
        self.darray.add("a")
        self.assertFalse(self.darray.isEmpty(), " array isEmpty should return fase")

    def test_contains(self):
        self.darray = DynamicArray(2)
        self.assertFalse(self.darray.array_contains("a"))
        self.darray.add("a")
        self.assertTrue(self.darray.array_contains("a"))
        self.darray.add("b")
        self.darray.add("b")
        self.darray.add("c")
        self.assertTrue(self.darray.array_contains("b"))
        self.assertTrue(self.darray.array_contains("c"))
        self.darray.delete(3)
        self.assertFalse(self.darray.array_contains("c"))
        self.darray.delete(2)
        self.assertTrue(self.darray.array_contains("b"))
        self.darray.delete(1)
        self.assertFalse(self.darray.array_contains("b"))
        self.darray.delete(0)
        self.assertFalse(self.darray.array_contains("a"))

if __name__ == '__main__':
    # print('working directory: ' + os.getcwd())
    unittest.main()



'''
OUTPUT:


data size: 2
size: 0
capacity: 2
capacity is: 2
printing method: add
index: 0 val: None
index: 1 val: None
size is: 0
capacity is: 2
capacity is: 2
printing method: add
index: 0 val: a
index: 1 val: None
size is: 1
capacity is: 2
capacity is: 2
printing method: add
index: 0 val: a
index: 1 val: None
size is: 1
capacity is: 2
capacity is: 2
printing method: add
index: 0 val: a
index: 1 val: b
size is: 2
capacity is: 2
capacity is: 2
printing method: add
index: 0 val: a
index: 1 val: b
size is: 2
capacity is: 2
resizing!
capacity is: 4
printing method: add
index: 0 val: a
index: 1 val: b
index: 2 val: c
index: 3 val: None
size is: 3
capacity is: 4
capacity is: 4
printing method: delete
index: 0 val: a
index: 1 val: b
index: 2 val: c
index: 3 val: None
size is: 3
capacity is: 4
capacity is: 4
printing method: delete
index: 0 val: b
index: 1 val: c
index: 2 val: None
index: 3 val: None
size is: 2
capacity is: 4
size is: 2
.get and set...
initialized dynamic array.
data size: 2
size: 0
capacity: 2
resizing!
resizing!
resizing!
resizing!
resizing!
capacity is: 64
printing method: array_set
index: 0 val: None
index: 1 val: None
index: 2 val: None
index: 3 val: None
index: 4 val: None
index: 5 val: None
index: 6 val: None
index: 7 val: None
index: 8 val: None
index: 9 val: None
index: 10 val: None
index: 11 val: None
index: 12 val: None
index: 13 val: None
index: 14 val: None
index: 15 val: None
index: 16 val: None
index: 17 val: None
index: 18 val: None
index: 19 val: None
index: 20 val: None
index: 21 val: None
index: 22 val: None
index: 23 val: None
index: 24 val: None
index: 25 val: None
index: 26 val: None
index: 27 val: None
index: 28 val: None
index: 29 val: None
index: 30 val: None
index: 31 val: None
index: 32 val: None
index: 33 val: None
index: 34 val: None
index: 35 val: None
index: 36 val: None
index: 37 val: None
index: 38 val: None
index: 39 val: None
index: 40 val: None
index: 41 val: None
index: 42 val: a
index: 43 val: None
index: 44 val: None
index: 45 val: None
index: 46 val: None
index: 47 val: None
index: 48 val: None
index: 49 val: None
index: 50 val: None
index: 51 val: None
index: 52 val: None
index: 53 val: None
index: 54 val: None
index: 55 val: None
index: 56 val: None
index: 57 val: None
index: 58 val: None
index: 59 val: None
index: 60 val: None
index: 61 val: None
index: 62 val: None
index: 63 val: None
size is: 42
capacity is: 64
.initialized dynamic array.
data size: 2
size: 0
capacity: 2
.initialized dynamic array.
data size: 2
size: 0
capacity: 2
array_contains...
value to search for is: a
capacity is: 2
printing method: add
index: 0 val: None
index: 1 val: None
size is: 0
capacity is: 2
capacity is: 2
printing method: add
index: 0 val: a
index: 1 val: None
size is: 1
capacity is: 2
array_contains...
value to search for is: a
capacity is: 2
printing method: add
index: 0 val: a
index: 1 val: None
size is: 1
capacity is: 2
capacity is: 2
printing method: add
index: 0 val: a
index: 1 val: b
size is: 2
capacity is: 2
capacity is: 2
printing method: add
index: 0 val: a
index: 1 val: b
size is: 2
capacity is: 2
resizing!
capacity is: 4
printing method: add
index: 0 val: a
index: 1 val: b
index: 2 val: b
index: 3 val: None
size is: 3
capacity is: 4
capacity is: 4
printing method: add
index: 0 val: a
index: 1 val: b
index: 2 val: b
index: 3 val: None
size is: 3
capacity is: 4
capacity is: 4
printing method: add
index: 0 val: a
index: 1 val: b
index: 2 val: b
index: 3 val: c
size is: 4
capacity is: 4
array_contains...
value to search for is: b
array_contains...
value to search for is: c
capacity is: 4
printing method: delete
index: 0 val: a
index: 1 val: b
index: 2 val: b
index: 3 val: c
size is: 4
capacity is: 4
capacity is: 4
printing method: delete
index: 0 val: a
index: 1 val: b
index: 2 val: b
index: 3 val: None
size is: 3
capacity is: 4
array_contains...
value to search for is: c
capacity is: 4
printing method: delete
index: 0 val: a
index: 1 val: b
index: 2 val: b
index: 3 val: None
size is: 3
capacity is: 4
capacity is: 4
printing method: delete
index: 0 val: a
index: 1 val: b
index: 2 val: None
index: 3 val: None
size is: 2
capacity is: 4
array_contains...
value to search for is: b
capacity is: 4
printing method: delete
index: 0 val: a
index: 1 val: b
index: 2 val: None
index: 3 val: None
size is: 2
capacity is: 4
capacity is: 4
printing method: delete
index: 0 val: a
index: 1 val: None
index: 2 val: None
index: 3 val: None
size is: 1
capacity is: 4
array_contains...
value to search for is: b
capacity is: 4
printing method: delete
index: 0 val: a
index: 1 val: None
index: 2 val: None
index: 3 val: None
size is: 1
capacity is: 4
capacity is: 4
printing method: delete
index: 0 val: None
index: 1 val: None
index: 2 val: None
index: 3 val: None
size is: 0
capacity is: 4
array_contains...
value to search for is: a
.testing delete last
initialized dynamic array.
data size: 2
size: 0
capacity: 2
capacity is: 2
printing method: add
index: 0 val: None
index: 1 val: None
size is: 0
capacity is: 2
capacity is: 2
printing method: add
index: 0 val: a
index: 1 val: None
size is: 1
capacity is: 2
capacity is: 2
printing method: add
index: 0 val: a
index: 1 val: None
size is: 1
capacity is: 2
capacity is: 2
printing method: add
index: 0 val: a
index: 1 val: b
size is: 2
capacity is: 2
capacity is: 2
printing method: add
index: 0 val: a
index: 1 val: b
size is: 2
capacity is: 2
resizing!
capacity is: 4
printing method: add
index: 0 val: a
index: 1 val: b
index: 2 val: c
index: 3 val: None
size is: 3
capacity is: 4
capacity is: 4
printing method: delete
index: 0 val: a
index: 1 val: b
index: 2 val: c
index: 3 val: None
size is: 3
capacity is: 4
capacity is: 4
printing method: delete
index: 0 val: a
index: 1 val: b
index: 2 val: None
index: 3 val: None
size is: 2
capacity is: 4
size is: 2
.initialized dynamic array.
data size: 2
size: 0
capacity: 2
testing delete middle
capacity is: 2
printing method: add
index: 0 val: None
index: 1 val: None
size is: 0
capacity is: 2
capacity is: 2
printing method: add
index: 0 val: a
index: 1 val: None
size is: 1
capacity is: 2
capacity is: 2
printing method: add
index: 0 val: a
index: 1 val: None
size is: 1
capacity is: 2
capacity is: 2
printing method: add
index: 0 val: a
index: 1 val: b
size is: 2
capacity is: 2
capacity is: 2
printing method: add
index: 0 val: a
index: 1 val: b
size is: 2
capacity is: 2
resizing!
capacity is: 4
printing method: add
index: 0 val: a
index: 1 val: b
index: 2 val: c
index: 3 val: None
size is: 3
capacity is: 4
capacity is: 4
printing method: delete
index: 0 val: a
index: 1 val: b
index: 2 val: c
index: 3 val: None
size is: 3
capacity is: 4
capacity is: 4
printing method: delete
index: 0 val: a
index: 1 val: c
index: 2 val: None
index: 3 val: None
size is: 2
capacity is: 4
size is: 2
.initialized dynamic array.
data size: 2
size: 0
capacity: 2
.initialized dynamic array.
data size: 2
size: 0
capacity: 2
capacity is: 2
printing method: add
index: 0 val: None
index: 1 val: None
size is: 0
capacity is: 2
capacity is: 2
printing method: add
index: 0 val: a
index: 1 val: None
size is: 1
capacity is: 2
capacity is: 2
printing method: add
index: 0 val: a
index: 1 val: None
size is: 1
capacity is: 2
capacity is: 2
printing method: add
index: 0 val: a
index: 1 val: b
size is: 2
capacity is: 2
capacity is: 2
printing method: add
index: 0 val: a
index: 1 val: b
size is: 2
capacity is: 2
resizing!
capacity is: 4
printing method: add
index: 0 val: a
index: 1 val: b
index: 2 val: c
index: 3 val: None
size is: 3
capacity is: 4
capacity is: 4
printing method: insert
index: 0 val: a
index: 1 val: b
index: 2 val: c
index: 3 val: None
size is: 3
capacity is: 4
capacity is: 4
printing method: insert
index: 0 val: a
index: 1 val: b
index: 2 val: c
index: 3 val: c
size is: 3
capacity is: 4
capacity is: 4
printing method: insert
index: 0 val: a
index: 1 val: b
index: 2 val: b
index: 3 val: c
size is: 3
capacity is: 4
capacity is: 4
printing method: insert
index: 0 val: a
index: 1 val: d
index: 2 val: b
index: 3 val: c
size is: 4
capacity is: 4
size is: 4
.initialized dynamic array.
data size: 2
size: 0
capacity: 2
capacity is: 2
printing method: add
index: 0 val: None
index: 1 val: None
size is: 0
capacity is: 2
capacity is: 2
printing method: add
index: 0 val: a
index: 1 val: None
size is: 1
capacity is: 2
.
----------------------------------------------------------------------
Ran 9 tests in 0.039s

OK

'''