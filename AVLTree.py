# Andre Doumad

import sys, unittest
# Node
class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

    # min
    def min(self):
        if self.left:
            return self.left.min()
        return self

# Tree
class Tree(object):

    # insert
    def insert(self, node, key, value):
        if not node:
            return Node(key, value)
        elif node.key < key:
            node.right = self.insert(node.right, key, value)
        elif node.key > key:
            node.left = self.insert(node.left, key, value)
        elif key == node.key:
            node.value = value
        
        node.height = 1+max(self.getHeight(node.left),self.getHeight(node.right))
        balance = self.getBalance(node)

        if balance > 1:
            if node.left.key > key:
                return self.rotateRight(node)
            else:
                node.left = self.rotateLeft(node.left)
                return self.rotateRight(node)
        if balance < -1:
            if node.right.key < key:
                return self.rotateLeft(node)
            else:
                node.right = self.rotateRight(node.right)
                return self.rotateLeft(node)
        
        return node

    # delete
    def delete(self, node, key):
        print('deleting ' + str(key))
        if node == None:
            return None
        elif node.key < key:
            node.right = self.delete(node.right, key)
        elif node.key > key:
            node.left = self.delete(node.left, key)
        elif node.key == key:
            if node.left == None and node.right == None:
                print('no children')
                node = None
            elif node.left != None and node.right != None:
                print('two children')
                minRight = node.right.min()
                node.key = minRight.key
                node.value = minRight.value
                node.right = self.delete(node.right, key)
            elif node.right != None:
                print('right child')
                node = node.right
            elif node.left != None:
                print('left child')
                node = node.left
        return node

    # find
    def find(self, node, key):
        print('finding ' + str(key))
        if node == None:
            return None
        if node.key > key:
            return self.find(node.left, key)
        if node.key < key:
            return self.find(node.right, key)
        if node.key == key:
            print('found: ' + str(node.key))
            return node

    # get height
    def getHeight(self, node):
        if node:
            return node.height
        return 0

    # get balance
    def getBalance(self, node):
        if node:
            return self.getHeight(node.left) - self.getHeight(node.right)
        return 0

    # rotate right
    def rotateRight(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1+max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1+max(self.getHeight(y.left),self.getHeight(y.right))
        return y

    # rotate left
    def rotateLeft(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1+max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1+max(self.getHeight(y.left),self.getHeight(y.right))
        return y

    # print tree
    def printTree(self, node, indent, last):
        if node:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write('R----')
                indent += '     '
            else:
                sys.stdout.write('L----')
                indent += '|----'
            print(str(node.key) + ' ' + str(node.value))
            self.printTree(node.left, indent, False)
            self.printTree(node.right, indent, True)

# unittest
class unitTest(unittest.TestCase):
    tree = Tree()
    root = None
    # insert values
    for i in range(0, 50):
        root = tree.insert(root, i, str('Andre_' + str(i)))
    for i in reversed(range(50, 100)):
        root = tree.insert(root, i, str('Andre_' + str(i)))
    # print values
    tree.printTree(root, "", True)
    # find values
    node = tree.find(root, 12)
    print('found : ' + str(node.key) + ' ' + str(node.value))
    # delete values
    root = tree.delete(root, 5)
    tree.printTree(root, "", True)
    root = tree.delete(root, 11)
    tree.printTree(root, "", True)
    root = tree.delete(root, 29)
    tree.printTree(root, "", True)
    root = tree.delete(root, 14)
    tree.printTree(root, "", True)
    # find values
    node = tree.find(root, 9)
    root = tree.insert(root, 7, 'test modify value')
    tree.printTree(root, "", True)

if __name__ == "__main__":
    unittest.main()

'''
OUTPUT: 





R----47 Andre_47
     L----31 Andre_31
     |----L----15 Andre_15
     |----|----L----7 Andre_7
     |----|----|----L----3 Andre_3
     |----|----|----|----L----1 Andre_1
     |----|----|----|----|----L----0 Andre_0
     |----|----|----|----|----R----2 Andre_2
     |----|----|----|----R----5 Andre_5
     |----|----|----|----     L----4 Andre_4
     |----|----|----|----     R----6 Andre_6
     |----|----|----R----11 Andre_11
     |----|----|----     L----9 Andre_9
     |----|----|----     |----L----8 Andre_8
     |----|----|----     |----R----10 Andre_10
     |----|----|----     R----13 Andre_13
     |----|----|----          L----12 Andre_12
     |----|----|----          R----14 Andre_14
     |----|----R----23 Andre_23
     |----|----     L----19 Andre_19
     |----|----     |----L----17 Andre_17
     |----|----     |----|----L----16 Andre_16
     |----|----     |----|----R----18 Andre_18
     |----|----     |----R----21 Andre_21
     |----|----     |----     L----20 Andre_20
     |----|----     |----     R----22 Andre_22
     |----|----     R----27 Andre_27
     |----|----          L----25 Andre_25
     |----|----          |----L----24 Andre_24
     |----|----          |----R----26 Andre_26
     |----|----          R----29 Andre_29
     |----|----               L----28 Andre_28
     |----|----               R----30 Andre_30
     |----R----39 Andre_39
     |----     L----35 Andre_35
     |----     |----L----33 Andre_33
     |----     |----|----L----32 Andre_32
     |----     |----|----R----34 Andre_34
     |----     |----R----37 Andre_37
     |----     |----     L----36 Andre_36
     |----     |----     R----38 Andre_38
     |----     R----43 Andre_43
     |----          L----41 Andre_41
     |----          |----L----40 Andre_40
     |----          |----R----42 Andre_42
     |----          R----45 Andre_45
     |----               L----44 Andre_44
     |----               R----46 Andre_46
     R----82 Andre_82
          L----70 Andre_70
          |----L----58 Andre_58
          |----|----L----52 Andre_52
          |----|----|----L----49 Andre_49
          |----|----|----|----L----48 Andre_48
          |----|----|----|----R----51 Andre_51
          |----|----|----|----     L----50 Andre_50
          |----|----|----R----55 Andre_55
          |----|----|----     L----53 Andre_53
          |----|----|----     |----R----54 Andre_54
          |----|----|----     R----56 Andre_56
          |----|----|----          R----57 Andre_57
          |----|----R----64 Andre_64
          |----|----     L----61 Andre_61
          |----|----     |----L----59 Andre_59
          |----|----     |----|----R----60 Andre_60
          |----|----     |----R----62 Andre_62
          |----|----     |----     R----63 Andre_63
          |----|----     R----67 Andre_67
          |----|----          L----65 Andre_65
          |----|----          |----R----66 Andre_66
          |----|----          R----68 Andre_68
          |----|----               R----69 Andre_69
          |----R----76 Andre_76
          |----     L----73 Andre_73
          |----     |----L----71 Andre_71
          |----     |----|----R----72 Andre_72
          |----     |----R----74 Andre_74
          |----     |----     R----75 Andre_75
          |----     R----79 Andre_79
          |----          L----77 Andre_77
          |----          |----R----78 Andre_78
          |----          R----80 Andre_80
          |----               R----81 Andre_81
          R----88 Andre_88
               L----85 Andre_85
               |----L----83 Andre_83
               |----|----R----84 Andre_84
               |----R----86 Andre_86
               |----     R----87 Andre_87
               R----94 Andre_94
                    L----91 Andre_91
                    |----L----89 Andre_89
                    |----|----R----90 Andre_90
                    |----R----92 Andre_92
                    |----     R----93 Andre_93
                    R----97 Andre_97
                         L----95 Andre_95
                         |----R----96 Andre_96
                         R----98 Andre_98
                              R----99 Andre_99
finding 12
finding 12
finding 12
finding 12
finding 12
finding 12
finding 12
found: 12
found : 12 Andre_12
deleting 5
deleting 5
deleting 5
deleting 5
deleting 5
deleting 5
two children
deleting 5
deleting 5
R----47 Andre_47
     L----31 Andre_31
     |----L----15 Andre_15
     |----|----L----7 Andre_7
     |----|----|----L----3 Andre_3
     |----|----|----|----L----1 Andre_1
     |----|----|----|----|----L----0 Andre_0
     |----|----|----|----|----R----2 Andre_2
     |----|----|----|----R----6 Andre_6
     |----|----|----|----     L----4 Andre_4
     |----|----|----|----     R----6 Andre_6
     |----|----|----R----11 Andre_11
     |----|----|----     L----9 Andre_9
     |----|----|----     |----L----8 Andre_8
     |----|----|----     |----R----10 Andre_10
     |----|----|----     R----13 Andre_13
     |----|----|----          L----12 Andre_12
     |----|----|----          R----14 Andre_14
     |----|----R----23 Andre_23
     |----|----     L----19 Andre_19
     |----|----     |----L----17 Andre_17
     |----|----     |----|----L----16 Andre_16
     |----|----     |----|----R----18 Andre_18
     |----|----     |----R----21 Andre_21
     |----|----     |----     L----20 Andre_20
     |----|----     |----     R----22 Andre_22
     |----|----     R----27 Andre_27
     |----|----          L----25 Andre_25
     |----|----          |----L----24 Andre_24
     |----|----          |----R----26 Andre_26
     |----|----          R----29 Andre_29
     |----|----               L----28 Andre_28
     |----|----               R----30 Andre_30
     |----R----39 Andre_39
     |----     L----35 Andre_35
     |----     |----L----33 Andre_33
     |----     |----|----L----32 Andre_32
     |----     |----|----R----34 Andre_34
     |----     |----R----37 Andre_37
     |----     |----     L----36 Andre_36
     |----     |----     R----38 Andre_38
     |----     R----43 Andre_43
     |----          L----41 Andre_41
     |----          |----L----40 Andre_40
     |----          |----R----42 Andre_42
     |----          R----45 Andre_45
     |----               L----44 Andre_44
     |----               R----46 Andre_46
     R----82 Andre_82
          L----70 Andre_70
          |----L----58 Andre_58
          |----|----L----52 Andre_52
          |----|----|----L----49 Andre_49
          |----|----|----|----L----48 Andre_48
          |----|----|----|----R----51 Andre_51
          |----|----|----|----     L----50 Andre_50
          |----|----|----R----55 Andre_55
          |----|----|----     L----53 Andre_53
          |----|----|----     |----R----54 Andre_54
          |----|----|----     R----56 Andre_56
          |----|----|----          R----57 Andre_57
          |----|----R----64 Andre_64
          |----|----     L----61 Andre_61
          |----|----     |----L----59 Andre_59
          |----|----     |----|----R----60 Andre_60
          |----|----     |----R----62 Andre_62
          |----|----     |----     R----63 Andre_63
          |----|----     R----67 Andre_67
          |----|----          L----65 Andre_65
          |----|----          |----R----66 Andre_66
          |----|----          R----68 Andre_68
          |----|----               R----69 Andre_69
          |----R----76 Andre_76
          |----     L----73 Andre_73
          |----     |----L----71 Andre_71
          |----     |----|----R----72 Andre_72
          |----     |----R----74 Andre_74
          |----     |----     R----75 Andre_75
          |----     R----79 Andre_79
          |----          L----77 Andre_77
          |----          |----R----78 Andre_78
          |----          R----80 Andre_80
          |----               R----81 Andre_81
          R----88 Andre_88
               L----85 Andre_85
               |----L----83 Andre_83
               |----|----R----84 Andre_84
               |----R----86 Andre_86
               |----     R----87 Andre_87
               R----94 Andre_94
                    L----91 Andre_91
                    |----L----89 Andre_89
                    |----|----R----90 Andre_90
                    |----R----92 Andre_92
                    |----     R----93 Andre_93
                    R----97 Andre_97
                         L----95 Andre_95
                         |----R----96 Andre_96
                         R----98 Andre_98
                              R----99 Andre_99
deleting 11
deleting 11
deleting 11
deleting 11
deleting 11
two children
deleting 11
deleting 11
deleting 11
R----47 Andre_47
     L----31 Andre_31
     |----L----15 Andre_15
     |----|----L----7 Andre_7
     |----|----|----L----3 Andre_3
     |----|----|----|----L----1 Andre_1
     |----|----|----|----|----L----0 Andre_0
     |----|----|----|----|----R----2 Andre_2
     |----|----|----|----R----6 Andre_6
     |----|----|----|----     L----4 Andre_4
     |----|----|----|----     R----6 Andre_6
     |----|----|----R----12 Andre_12
     |----|----|----     L----9 Andre_9
     |----|----|----     |----L----8 Andre_8
     |----|----|----     |----R----10 Andre_10
     |----|----|----     R----13 Andre_13
     |----|----|----          L----12 Andre_12
     |----|----|----          R----14 Andre_14
     |----|----R----23 Andre_23
     |----|----     L----19 Andre_19
     |----|----     |----L----17 Andre_17
     |----|----     |----|----L----16 Andre_16
     |----|----     |----|----R----18 Andre_18
     |----|----     |----R----21 Andre_21
     |----|----     |----     L----20 Andre_20
     |----|----     |----     R----22 Andre_22
     |----|----     R----27 Andre_27
     |----|----          L----25 Andre_25
     |----|----          |----L----24 Andre_24
     |----|----          |----R----26 Andre_26
     |----|----          R----29 Andre_29
     |----|----               L----28 Andre_28
     |----|----               R----30 Andre_30
     |----R----39 Andre_39
     |----     L----35 Andre_35
     |----     |----L----33 Andre_33
     |----     |----|----L----32 Andre_32
     |----     |----|----R----34 Andre_34
     |----     |----R----37 Andre_37
     |----     |----     L----36 Andre_36
     |----     |----     R----38 Andre_38
     |----     R----43 Andre_43
     |----          L----41 Andre_41
     |----          |----L----40 Andre_40
     |----          |----R----42 Andre_42
     |----          R----45 Andre_45
     |----               L----44 Andre_44
     |----               R----46 Andre_46
     R----82 Andre_82
          L----70 Andre_70
          |----L----58 Andre_58
          |----|----L----52 Andre_52
          |----|----|----L----49 Andre_49
          |----|----|----|----L----48 Andre_48
          |----|----|----|----R----51 Andre_51
          |----|----|----|----     L----50 Andre_50
          |----|----|----R----55 Andre_55
          |----|----|----     L----53 Andre_53
          |----|----|----     |----R----54 Andre_54
          |----|----|----     R----56 Andre_56
          |----|----|----          R----57 Andre_57
          |----|----R----64 Andre_64
          |----|----     L----61 Andre_61
          |----|----     |----L----59 Andre_59
          |----|----     |----|----R----60 Andre_60
          |----|----     |----R----62 Andre_62
          |----|----     |----     R----63 Andre_63
          |----|----     R----67 Andre_67
          |----|----          L----65 Andre_65
          |----|----          |----R----66 Andre_66
          |----|----          R----68 Andre_68
          |----|----               R----69 Andre_69
          |----R----76 Andre_76
          |----     L----73 Andre_73
          |----     |----L----71 Andre_71
          |----     |----|----R----72 Andre_72
          |----     |----R----74 Andre_74
          |----     |----     R----75 Andre_75
          |----     R----79 Andre_79
          |----          L----77 Andre_77
          |----          |----R----78 Andre_78
          |----          R----80 Andre_80
          |----               R----81 Andre_81
          R----88 Andre_88
               L----85 Andre_85
               |----L----83 Andre_83
               |----|----R----84 Andre_84
               |----R----86 Andre_86
               |----     R----87 Andre_87
               R----94 Andre_94
                    L----91 Andre_91
                    |----L----89 Andre_89
                    |----|----R----90 Andre_90
                    |----R----92 Andre_92
                    |----     R----93 Andre_93
                    R----97 Andre_97
                         L----95 Andre_95
                         |----R----96 Andre_96
                         R----98 Andre_98
                              R----99 Andre_99
deleting 29
deleting 29
deleting 29
deleting 29
deleting 29
deleting 29
two children
deleting 29
deleting 29
R----47 Andre_47
     L----31 Andre_31
     |----L----15 Andre_15
     |----|----L----7 Andre_7
     |----|----|----L----3 Andre_3
     |----|----|----|----L----1 Andre_1
     |----|----|----|----|----L----0 Andre_0
     |----|----|----|----|----R----2 Andre_2
     |----|----|----|----R----6 Andre_6
     |----|----|----|----     L----4 Andre_4
     |----|----|----|----     R----6 Andre_6
     |----|----|----R----12 Andre_12
     |----|----|----     L----9 Andre_9
     |----|----|----     |----L----8 Andre_8
     |----|----|----     |----R----10 Andre_10
     |----|----|----     R----13 Andre_13
     |----|----|----          L----12 Andre_12
     |----|----|----          R----14 Andre_14
     |----|----R----23 Andre_23
     |----|----     L----19 Andre_19
     |----|----     |----L----17 Andre_17
     |----|----     |----|----L----16 Andre_16
     |----|----     |----|----R----18 Andre_18
     |----|----     |----R----21 Andre_21
     |----|----     |----     L----20 Andre_20
     |----|----     |----     R----22 Andre_22
     |----|----     R----27 Andre_27
     |----|----          L----25 Andre_25
     |----|----          |----L----24 Andre_24
     |----|----          |----R----26 Andre_26
     |----|----          R----30 Andre_30
     |----|----               L----28 Andre_28
     |----|----               R----30 Andre_30
     |----R----39 Andre_39
     |----     L----35 Andre_35
     |----     |----L----33 Andre_33
     |----     |----|----L----32 Andre_32
     |----     |----|----R----34 Andre_34
     |----     |----R----37 Andre_37
     |----     |----     L----36 Andre_36
     |----     |----     R----38 Andre_38
     |----     R----43 Andre_43
     |----          L----41 Andre_41
     |----          |----L----40 Andre_40
     |----          |----R----42 Andre_42
     |----          R----45 Andre_45
     |----               L----44 Andre_44
     |----               R----46 Andre_46
     R----82 Andre_82
          L----70 Andre_70
          |----L----58 Andre_58
          |----|----L----52 Andre_52
          |----|----|----L----49 Andre_49
          |----|----|----|----L----48 Andre_48
          |----|----|----|----R----51 Andre_51
          |----|----|----|----     L----50 Andre_50
          |----|----|----R----55 Andre_55
          |----|----|----     L----53 Andre_53
          |----|----|----     |----R----54 Andre_54
          |----|----|----     R----56 Andre_56
          |----|----|----          R----57 Andre_57
          |----|----R----64 Andre_64
          |----|----     L----61 Andre_61
          |----|----     |----L----59 Andre_59
          |----|----     |----|----R----60 Andre_60
          |----|----     |----R----62 Andre_62
          |----|----     |----     R----63 Andre_63
          |----|----     R----67 Andre_67
          |----|----          L----65 Andre_65
          |----|----          |----R----66 Andre_66
          |----|----          R----68 Andre_68
          |----|----               R----69 Andre_69
          |----R----76 Andre_76
          |----     L----73 Andre_73
          |----     |----L----71 Andre_71
          |----     |----|----R----72 Andre_72
          |----     |----R----74 Andre_74
          |----     |----     R----75 Andre_75
          |----     R----79 Andre_79
          |----          L----77 Andre_77
          |----          |----R----78 Andre_78
          |----          R----80 Andre_80
          |----               R----81 Andre_81
          R----88 Andre_88
               L----85 Andre_85
               |----L----83 Andre_83
               |----|----R----84 Andre_84
               |----R----86 Andre_86
               |----     R----87 Andre_87
               R----94 Andre_94
                    L----91 Andre_91
                    |----L----89 Andre_89
                    |----|----R----90 Andre_90
                    |----R----92 Andre_92
                    |----     R----93 Andre_93
                    R----97 Andre_97
                         L----95 Andre_95
                         |----R----96 Andre_96
                         R----98 Andre_98
                              R----99 Andre_99
deleting 14
deleting 14
deleting 14
deleting 14
deleting 14
deleting 14
deleting 14
no children
R----47 Andre_47
     L----31 Andre_31
     |----L----15 Andre_15
     |----|----L----7 Andre_7
     |----|----|----L----3 Andre_3
     |----|----|----|----L----1 Andre_1
     |----|----|----|----|----L----0 Andre_0
     |----|----|----|----|----R----2 Andre_2
     |----|----|----|----R----6 Andre_6
     |----|----|----|----     L----4 Andre_4
     |----|----|----|----     R----6 Andre_6
     |----|----|----R----12 Andre_12
     |----|----|----     L----9 Andre_9
     |----|----|----     |----L----8 Andre_8
     |----|----|----     |----R----10 Andre_10
     |----|----|----     R----13 Andre_13
     |----|----|----          L----12 Andre_12
     |----|----R----23 Andre_23
     |----|----     L----19 Andre_19
     |----|----     |----L----17 Andre_17
     |----|----     |----|----L----16 Andre_16
     |----|----     |----|----R----18 Andre_18
     |----|----     |----R----21 Andre_21
     |----|----     |----     L----20 Andre_20
     |----|----     |----     R----22 Andre_22
     |----|----     R----27 Andre_27
     |----|----          L----25 Andre_25
     |----|----          |----L----24 Andre_24
     |----|----          |----R----26 Andre_26
     |----|----          R----30 Andre_30
     |----|----               L----28 Andre_28
     |----|----               R----30 Andre_30
     |----R----39 Andre_39
     |----     L----35 Andre_35
     |----     |----L----33 Andre_33
     |----     |----|----L----32 Andre_32
     |----     |----|----R----34 Andre_34
     |----     |----R----37 Andre_37
     |----     |----     L----36 Andre_36
     |----     |----     R----38 Andre_38
     |----     R----43 Andre_43
     |----          L----41 Andre_41
     |----          |----L----40 Andre_40
     |----          |----R----42 Andre_42
     |----          R----45 Andre_45
     |----               L----44 Andre_44
     |----               R----46 Andre_46
     R----82 Andre_82
          L----70 Andre_70
          |----L----58 Andre_58
          |----|----L----52 Andre_52
          |----|----|----L----49 Andre_49
          |----|----|----|----L----48 Andre_48
          |----|----|----|----R----51 Andre_51
          |----|----|----|----     L----50 Andre_50
          |----|----|----R----55 Andre_55
          |----|----|----     L----53 Andre_53
          |----|----|----     |----R----54 Andre_54
          |----|----|----     R----56 Andre_56
          |----|----|----          R----57 Andre_57
          |----|----R----64 Andre_64
          |----|----     L----61 Andre_61
          |----|----     |----L----59 Andre_59
          |----|----     |----|----R----60 Andre_60
          |----|----     |----R----62 Andre_62
          |----|----     |----     R----63 Andre_63
          |----|----     R----67 Andre_67
          |----|----          L----65 Andre_65
          |----|----          |----R----66 Andre_66
          |----|----          R----68 Andre_68
          |----|----               R----69 Andre_69
          |----R----76 Andre_76
          |----     L----73 Andre_73
          |----     |----L----71 Andre_71
          |----     |----|----R----72 Andre_72
          |----     |----R----74 Andre_74
          |----     |----     R----75 Andre_75
          |----     R----79 Andre_79
          |----          L----77 Andre_77
          |----          |----R----78 Andre_78
          |----          R----80 Andre_80
          |----               R----81 Andre_81
          R----88 Andre_88
               L----85 Andre_85
               |----L----83 Andre_83
               |----|----R----84 Andre_84
               |----R----86 Andre_86
               |----     R----87 Andre_87
               R----94 Andre_94
                    L----91 Andre_91
                    |----L----89 Andre_89
                    |----|----R----90 Andre_90
                    |----R----92 Andre_92
                    |----     R----93 Andre_93
                    R----97 Andre_97
                         L----95 Andre_95
                         |----R----96 Andre_96
                         R----98 Andre_98
                              R----99 Andre_99
finding 9
finding 9
finding 9
finding 9
finding 9
finding 9
found: 9
R----47 Andre_47
     L----31 Andre_31
     |----L----15 Andre_15
     |----|----L----7 test modify value
     |----|----|----L----3 Andre_3
     |----|----|----|----L----1 Andre_1
     |----|----|----|----|----L----0 Andre_0
     |----|----|----|----|----R----2 Andre_2
     |----|----|----|----R----6 Andre_6
     |----|----|----|----     L----4 Andre_4
     |----|----|----|----     R----6 Andre_6
     |----|----|----R----12 Andre_12
     |----|----|----     L----9 Andre_9
     |----|----|----     |----L----8 Andre_8
     |----|----|----     |----R----10 Andre_10
     |----|----|----     R----13 Andre_13
     |----|----|----          L----12 Andre_12
     |----|----R----23 Andre_23
     |----|----     L----19 Andre_19
     |----|----     |----L----17 Andre_17
     |----|----     |----|----L----16 Andre_16
     |----|----     |----|----R----18 Andre_18
     |----|----     |----R----21 Andre_21
     |----|----     |----     L----20 Andre_20
     |----|----     |----     R----22 Andre_22
     |----|----     R----27 Andre_27
     |----|----          L----25 Andre_25
     |----|----          |----L----24 Andre_24
     |----|----          |----R----26 Andre_26
     |----|----          R----30 Andre_30
     |----|----               L----28 Andre_28
     |----|----               R----30 Andre_30
     |----R----39 Andre_39
     |----     L----35 Andre_35
     |----     |----L----33 Andre_33
     |----     |----|----L----32 Andre_32
     |----     |----|----R----34 Andre_34
     |----     |----R----37 Andre_37
     |----     |----     L----36 Andre_36
     |----     |----     R----38 Andre_38
     |----     R----43 Andre_43
     |----          L----41 Andre_41
     |----          |----L----40 Andre_40
     |----          |----R----42 Andre_42
     |----          R----45 Andre_45
     |----               L----44 Andre_44
     |----               R----46 Andre_46
     R----82 Andre_82
          L----70 Andre_70
          |----L----58 Andre_58
          |----|----L----52 Andre_52
          |----|----|----L----49 Andre_49
          |----|----|----|----L----48 Andre_48
          |----|----|----|----R----51 Andre_51
          |----|----|----|----     L----50 Andre_50
          |----|----|----R----55 Andre_55
          |----|----|----     L----53 Andre_53
          |----|----|----     |----R----54 Andre_54
          |----|----|----     R----56 Andre_56
          |----|----|----          R----57 Andre_57
          |----|----R----64 Andre_64
          |----|----     L----61 Andre_61
          |----|----     |----L----59 Andre_59
          |----|----     |----|----R----60 Andre_60
          |----|----     |----R----62 Andre_62
          |----|----     |----     R----63 Andre_63
          |----|----     R----67 Andre_67
          |----|----          L----65 Andre_65
          |----|----          |----R----66 Andre_66
          |----|----          R----68 Andre_68
          |----|----               R----69 Andre_69
          |----R----76 Andre_76
          |----     L----73 Andre_73
          |----     |----L----71 Andre_71
          |----     |----|----R----72 Andre_72
          |----     |----R----74 Andre_74
          |----     |----     R----75 Andre_75
          |----     R----79 Andre_79
          |----          L----77 Andre_77
          |----          |----R----78 Andre_78
          |----          R----80 Andre_80
          |----               R----81 Andre_81
          R----88 Andre_88
               L----85 Andre_85
               |----L----83 Andre_83
               |----|----R----84 Andre_84
               |----R----86 Andre_86
               |----     R----87 Andre_87
               R----94 Andre_94
                    L----91 Andre_91
                    |----L----89 Andre_89
                    |----|----R----90 Andre_90
                    |----R----92 Andre_92
                    |----     R----93 Andre_93
                    R----97 Andre_97
                         L----95 Andre_95
                         |----R----96 Andre_96
                         R----98 Andre_98
                              R----99 Andre_99

----------------------------------------------------------------------
Ran 0 tests in 0.000s

OK


'''