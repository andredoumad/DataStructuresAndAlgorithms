# Andre Doumad

import unittest

class Node():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
    
    def min(self):
        if self.left:
            return self.left.min()
        else:
            return self
    
class BinarySearchTree():
    def __init__(self):
        self.root = None

    # insert
    def insert(self, key, value):
        if self.root == None:
            self.root = Node(key, value)
            return
        self.doInsert(self.root, key, value)

    def doInsert(self, node, key, value):
        if node.key > key:
            if node.left:
                return self.doInsert(node.left, key, value)
            else:
                node.left = Node(key, value)
        elif node.key < key:
            if node.right:
                return self.doInsert(node.right, key, value)
            else:
                node.right = Node(key, value)
        else:
            node.value = value


    # find
    def find(self, key):
        print('searched for key: ' + str(key))
        if self.root == None:
            return None

        node = self.doFind(self.root, key)
        if node == None:
            print('found none ')
            return None
        else:
            print('found ' + str(node.value))
            return node.value

    def doFind(self, node, key):
        if node.key == key: 
            return node
        if node.key > key:
            if node.left:
                return self.doFind(node.left, key)
            else:
                return None
        if node.key < key:
            if node.right:    
                return self.doFind(node.right, key)
            else:
                return None

    # delete
    def delete(self, key):
        if self.root == None:
            return None
        print('delete: ' + str(key))
        self.root = self.doDelete(self.root, key)
        
    def doDelete(self, node, key):
        if node == None:
            return None
        if node.key < key:
            node.right = self.doDelete(node.right, key)
        elif node.key > key:
            node.left = self.doDelete(node.left, key)
        elif node.key == key:
            # no children
            if node.left == None and node.right == None:
                print('no children')
                node = None

            # two children
            elif node.right != None and node.left != None:
                print('two children')
                minRight = node.right.min()
                node.key = minRight.key
                node.value = minRight.value
                node.right = self.doDelete(node.right, node.key)

            # delete one child
            elif node.right != None:
                print('right child')
                node = node.right
            elif node.left != None:
                print('left child')
                node = node.left
        return node



    # print
    def prettyPrint(self):
        print('---------------')
        print('prettyPrint')
        if self.root != None:
            self.doPrettyPrint(self.root, 0, [10])
        print('---------------')

    def doPrettyPrint(self, root, space, count):
        # base case
        if root == None:
            return

        space += count[0]
        # print('space = ' + str(space))
        # print('count = ' + str(count))

        # print right
        self.doPrettyPrint(root.right, space, count)

        print()
        for i in range(count[0], space):
            # print('i = ' + str(i))
            print(end= ' ')
        print(str(root.key) + ' ' + str(root.value))

        # print left
        self.doPrettyPrint(root.left, space, count)


    def inOrderTraversal(self):
        if self.root == None:
            return
        else:
            self.doInOrderTraversal(self.root)

    def doInOrderTraversal(self, node):
        if node != None:
            self.doInOrderTraversal(node.left)
            print(node.key)
            self.doInOrderTraversal(node.right)


    def postOrderTraversal(self):
        if self.root == None:
            return
        else:
            self.doPostOrderTraversal(self.root)

    def doPostOrderTraversal(self, node):
        if node != None:
            self.doPostOrderTraversal(node.left)
            self.doPostOrderTraversal(node.right)
            print(node.key)

    def preOrderTraversal(self):
        if self.root == None:
            return
        else:
            self.doPreOrderTraversal(self.root)
    
    def doPreOrderTraversal(self, node):
        if node != None:
            print(node.key)
            self.doPreOrderTraversal(node.left)
            self.doPreOrderTraversal(node.right)





class unitTest(unittest.TestCase):
    # test
    def test_a(self):
        bst = BinarySearchTree()
        bst.insert(100, 'this')
        bst.insert(150, 'is')
        bst.insert(50, 'how')
        bst.insert(175, 'file')
        bst.insert(125, 'systems')
        bst.insert(75, 'insert')
        bst.insert(25, 'find')
        bst.insert(200, 'update')
        bst.insert(165, 'and')
        bst.insert(135, 'delete')
        bst.insert(115, 'your')
        bst.insert(90, 'data')
        bst.insert(65, 'written')
        bst.insert(35, 'by')
        bst.insert(15, 'andre')
        bst.prettyPrint()
        bst.preOrderTraversal()
        bst.postOrderTraversal()
        bst.inOrderTraversal()
        bst.find(100)
        bst.find(115)
        bst.delete(100)
        bst.prettyPrint()
        bst.delete(25)
        bst.prettyPrint()
        self.assertEqual(bst.find(25), None, 'should equal None')
        bst.delete(100)
        bst.prettyPrint()
        self.assertEqual(bst.find(100), None, 'should equal None')
        self.assertEqual(bst.find(115), 'your', 'should equal your')
        bst.delete(175)
        bst.prettyPrint()
        self.assertEqual(bst.find(175), None, 'should equal None')
        self.assertEqual(bst.find(165), 'and', 'should equal and')
        bst.delete(150)
        bst.prettyPrint()
        self.assertEqual(bst.find(150), None, 'should equal None')
        self.assertEqual(bst.find(165), 'and', 'should equal and')
        bst.delete(50)
        bst.prettyPrint()
        self.assertEqual(bst.find(50), None, 'should equal None')
        self.assertEqual(bst.find(65), 'written', 'should equal written')


if __name__ == '__main__':
    unittest.main()


'''
OUTPUT:


---------------
prettyPrint

                              200 update

                    175 file

                              165 and

          150 is

                              135 delete

                    125 systems

                              115 your

100 this

                              90 data

                    75 insert

                              65 written

          50 how

                              35 by

                    25 find

                              15 andre
---------------
100
50
25
15
35
75
65
90
150
125
115
135
175
165
200
15
35
25
65
90
75
50
115
135
125
165
200
175
150
100
15
25
35
50
65
75
90
100
115
125
135
150
165
175
200
searched for key: 100
found this
searched for key: 115
found your
delete: 100
two children
no children
---------------
prettyPrint

                              200 update

                    175 file

                              165 and

          150 is

                              135 delete

                    125 systems

115 your

                              90 data

                    75 insert

                              65 written

          50 how

                              35 by

                    25 find

                              15 andre
---------------
delete: 25
two children
no children
---------------
prettyPrint

                              200 update

                    175 file

                              165 and

          150 is

                              135 delete

                    125 systems

115 your

                              90 data

                    75 insert

                              65 written

          50 how

                    35 by

                              15 andre
---------------
searched for key: 25
found none 
delete: 100
---------------
prettyPrint

                              200 update

                    175 file

                              165 and

          150 is

                              135 delete

                    125 systems

115 your

                              90 data

                    75 insert

                              65 written

          50 how

                    35 by

                              15 andre
---------------
searched for key: 100
found none 
searched for key: 115
found your
delete: 175
two children
no children
---------------
prettyPrint

                    200 update

                              165 and

          150 is

                              135 delete

                    125 systems

115 your

                              90 data

                    75 insert

                              65 written

          50 how

                    35 by

                              15 andre
---------------
searched for key: 175
found none 
searched for key: 165
found and
delete: 150
two children
no children
---------------
prettyPrint

                    200 update

          165 and

                              135 delete

                    125 systems

115 your

                              90 data

                    75 insert

                              65 written

          50 how

                    35 by

                              15 andre
---------------
searched for key: 150
found none 
searched for key: 165
found and
delete: 50
two children
no children
---------------
prettyPrint

                    200 update

          165 and

                              135 delete

                    125 systems

115 your

                              90 data

                    75 insert

          65 written

                    35 by

                              15 andre
---------------
searched for key: 50
found none 
searched for key: 65
found written
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

'''