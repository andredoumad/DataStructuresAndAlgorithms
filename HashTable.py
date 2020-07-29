# Andre Doumad

import unittest


class HashEntry():

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable():
    def __init__(self):
        self.initial_size = 16
        self.data = [None]*self.initial_size

    def put(self, key, value):
        index = self.getIndex(key)
        if self.data[index] == None:
            self.data[index] = HashEntry(key, value)
        else:
            currentNode = self.data[index]
            next = self.data[index].next
            while next != None:
                currentNode = self.data[index].next
                next = currentNode.next
            currentNode.next = HashEntry(key, value)

    def get(self, key):
        index = self.getIndex(key)

        if self.data[index] == None:
            return None
        else:
            currentNode = self.data[index]
            next = self.data[index].next
            if currentNode.key == key:
                return currentNode.value
            while next != None:
                currentNode = self.data[index].next
                if currentNode.key == key:
                    return currentNode.value
                next = currentNode.next

    def getIndex(self, key):

        if key == "John Smith" or key == "Sandra Dee":
            hashcode = 4
        else:
            hashcode = hash(key)

        index = int(hashcode % self.initial_size) 
        print('key: ' + str(key) + 'hashcode is: ' + str(hashcode) + ' index is: ' + str(index))
        return index



class TestHashTable(unittest.TestCase):

    def test_PushAndGet(self):
        print('test_PushAndGet')
        hashtable = HashTable()
        hashtable.put('andredoumad', 'god')
        self.assertEquals(hashtable.get('andredoumad'), 'god', 'Expected god')
        print('andre is ' + str(hashtable.get('andredoumad')))
        hashtable.put('John Smith', '521-1234')
        hashtable.put('Lisa Smith', '521-8976')
        hashtable.put('Sam Doe', '521-5030')
        hashtable.put('Sandra Dee', '521-9655')
        hashtable.put('Ted Baker', '418-4165')
        self.assertEquals(hashtable.get('John Smith'), '521-1234', 'Expected 521-1234')
        self.assertEquals(hashtable.get('Lisa Smith'), '521-8976', 'Expected 521-8976')
        self.assertEquals(hashtable.get('Sam Doe'), '521-5030', 'Expected 521-5030')
        self.assertEquals(hashtable.get('Sandra Dee'), '521-9655', 'Expected 521-9655')
        self.assertEquals(hashtable.get('Ted Baker'), '418-4165', 'Expected 418-4165')

    def test_Empty(self):
        print('test_Empty')
        hashtable = HashTable()
        self.assertEquals(hashtable.get('Ted baker'), None, 'Expected none')
        self.assertEquals(hashtable.get('Tim Lee'), None, 'Expected none')


    def test_Collision(self):
        print('test_Collision')
        hashtable = HashTable()
        hashtable.put('John Smith', "521-1234")
        hashtable.put('Sandra Dee', '521-9655')
        self.assertEquals(hashtable.get('John Smith'), '521-1234', 'should be john smith value')
        self.assertEquals(hashtable.get('Sandra Dee'), '521-9655', 'should be sandra dee value')
        self.assertEquals(hashtable.get('Tim Lee'), None, 'Should be none')
        
if __name__ == '__main__':
    unittest.main()

'''
OUTPUT: 

test_Collision
key: John Smithhashcode is: 4 index is: 4
key: Sandra Deehashcode is: 4 index is: 4
key: John Smithhashcode is: 4 index is: 4
/home/gordon/DataStructuresAndAlgorithms/HashTable.py:90: DeprecationWarning: Please use assertEqual instead.
  self.assertEquals(hashtable.get('John Smith'), '521-1234', 'should be john smith value')
key: Sandra Deehashcode is: 4 index is: 4
key: Tim Leehashcode is: -6083980269354857023 index is: 1
.test_Empty
key: Ted bakerhashcode is: -2112622546279262913 index is: 15
key: Tim Leehashcode is: -6083980269354857023 index is: 1
.test_PushAndGet
key: andredoumadhashcode is: -5409652610238313144 index is: 8
key: andredoumadhashcode is: -5409652610238313144 index is: 8
key: andredoumadhashcode is: -5409652610238313144 index is: 8
andre is god
key: John Smithhashcode is: 4 index is: 4
key: Lisa Smithhashcode is: 5014391903547772526 index is: 14
key: Sam Doehashcode is: 4883968730221999793 index is: 1
key: Sandra Deehashcode is: 4 index is: 4
key: Ted Bakerhashcode is: 2868536579733577853 index is: 13
key: John Smithhashcode is: 4 index is: 4
key: Lisa Smithhashcode is: 5014391903547772526 index is: 14
key: Sam Doehashcode is: 4883968730221999793 index is: 1
key: Sandra Deehashcode is: 4 index is: 4
key: Ted Bakerhashcode is: 2868536579733577853 index is: 13
.
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK

'''