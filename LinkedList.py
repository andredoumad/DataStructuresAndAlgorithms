# Andre Doumad

class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList():

    def __init__(self):
        # self.head = Node(None)
        self.head = None
        self.size = 0

    def addFront(self, data):
        print('addFront')
        newNode = Node(data)
        self.size += 1
        if self.head == None:
            self.head = newNode
            return

        newNode.next = self.head
        self.head = newNode

    def addBack(self, data):
        print('getBack')
        newNode = Node(data)
        self.size += 1
        if self.head == None:
            self.head = newNode
            return

        currentNode = self.head
        next = currentNode.next
        while next != None:
            currentNode = next
            next = currentNode.next

        currentNode.next = newNode

    def getFront(self):
        return self.head.data

    def getBack(self):
        print('getBack')
        currentNode = self.head
        next = currentNode.next
        while next != None:
            currentNode = next
            next = currentNode.next
        return currentNode.data

    # elegant approach
    def getSize(self):
        return self.size

    def clear(self):
        self.head = None
        self.size = 0

    def deleteValue(self, value):
        print('delete value')
        if self.head != None:
            currentNode = self.head
            next = currentNode.next
            currentValue = currentNode.data
            
            if currentValue == value:
                self.head = currentNode.next
                self.size -= 1
            else:
                while next != None:
                    if value == currentNode.next.data:
                        currentNode.next = currentNode.next.next
                        self.size -= 1
                    currentNode = currentNode.next
                    next = currentNode.next

    def print_list(self):
        if self.size > 0:
            print('print_list')
            currentNode = self.head
            next = currentNode.next
            while next != None:
                print('currentNode data: ' + str(currentNode.data))
                print('currentNode next: ' + str(currentNode.next))
                currentNode = next
                next = currentNode.next
            print('currentNode data: ' + str(currentNode.data))
            print('currentNode next: ' + str(currentNode.next))
        print('list size is 0')


import unittest, os, sys
from LinkedList import LinkedList

class LinkedListTest(unittest.TestCase):

    def test_AddFront(self):
        print('running test_AddFront')
        linkedlist = LinkedList()
        linkedlist.addFront(1)
        self.assertEqual(linkedlist.getFront(), 1, 'front should equal 1')

    def test_AddBack(self):
        print('running test_AddBack')
        linkedlist = LinkedList()
        linkedlist.addBack(2)
        self.assertEqual(linkedlist.getBack(), 2, 'front should equal 2')

    def test_GetBack(self):
        print('running test_AddFront')
        linkedlist = LinkedList()
        linkedlist.addFront(1)
        linkedlist.addFront(2)
        linkedlist.addFront(3)
        self.assertEqual(linkedlist.getBack(), 1, 'back should equal 1')

    def test_getSize(self):
        linkedlist = LinkedList()
        self.assertEqual(linkedlist.getSize(), 0, 'back should equal 0')
        linkedlist.addFront(3)
        linkedlist.addFront(2)
        linkedlist.addFront(1)
        self.assertEqual(linkedlist.getSize(), 3, 'back should equal 3')

    def test_clear(self):
        linkedlist = LinkedList()
        linkedlist.clear()
        self.assertEqual(linkedlist.getSize(), 0, 'should be 0' )
        self.assertEqual(linkedlist.getSize(), 0, 'back should equal 0')
        linkedlist.addFront(3)
        linkedlist.addFront(2)
        linkedlist.addFront(1)
        self.assertEqual(linkedlist.getSize(), 3, 'back should equal 3')


    def test_deleteValue(self):
        linkedlist = LinkedList()
        linkedlist.addBack(1)
        linkedlist.addBack(2)
        linkedlist.addBack(3)
        linkedlist.print_list()
        linkedlist.deleteValue(2)
        self.assertEqual(linkedlist.getSize(), 2, 'back should equal 2')
        self.assertEqual(linkedlist.getFront(), 1, 'back should equal 1')
        self.assertEqual(linkedlist.getBack(), 3, 'back should equal 3')
        linkedlist.print_list()


    def test_deleteHeadValue(self):
        linkedlist = LinkedList()
        linkedlist.addBack(1)
        linkedlist.print_list()
        self.assertEqual(linkedlist.getSize(), 1, 'back should equal 1')
        self.assertEqual(linkedlist.getFront(), 1, 'back should equal 1')
        linkedlist.deleteValue(1)
        self.assertEqual(linkedlist.getSize(), 0, 'back should equal 0')
        linkedlist.print_list()

if __name__ == '__main__':
    # print('working directory: ' + os.getcwd())
    unittest.main()


'''
OUTPUT: 

running test_AddBack
getBack
getBack
.running test_AddFront
addFront
.running test_AddFront
addFront
addFront
addFront
getBack
.addFront
addFront
addFront
.getBack
print_list
currentNode data: 1
currentNode next: None
list size is 0
delete value
list size is 0
.getBack
getBack
getBack
print_list
currentNode data: 1
currentNode next: <LinkedList.Node object at 0x7f6a7c2b2160>
currentNode data: 2
currentNode next: <LinkedList.Node object at 0x7f6a7c2b21c0>
currentNode data: 3
currentNode next: None
list size is 0
delete value
getBack
print_list
currentNode data: 1
currentNode next: <LinkedList.Node object at 0x7f6a7c2b21c0>
currentNode data: 3
currentNode next: None
list size is 0
.addFront
addFront
addFront
.
----------------------------------------------------------------------
Ran 7 tests in 0.000s

OK

'''
