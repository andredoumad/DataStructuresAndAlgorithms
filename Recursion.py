# Andre Doumad

'''

channel formatter

write a recursive algorithm that strips the leading zeros off strings of text.
simply strip off one zero at a time and then recursively call yourself until 
no leading zeros from the original string are left.

assertions
string in string out 
0001 = 1
0011 = 11
00001989 = 1989
VOD = VOD

'''

import unittest

class recursiveSolver(object):

    def solve(self, a):
        if len(a) > 1 and a[0] == '0':
            b = ''
            for i in range(1, len(a)):
                b += a[i]
            return self.solve(b)
        else:
            print('result: ' + str(a))
            return a
        
        # if a[0] == '0':
        #     print(str(a[1]))
        #     # return self.solve()


class unitTest(unittest.TestCase):
    def test_A(self):
        a = recursiveSolver()
        self.assertEqual(a.solve('0001'), '1', ' should equal 1')
        self.assertEqual(a.solve('0011'), '11', ' should equal 11')
        self.assertEqual(a.solve('00001989'), '1989', ' should equal 1989')
        self.assertEqual(a.solve('VOD'), 'VOD', ' should equal VOD')

if __name__ == '__main__':
    unittest.main()

'''

OUTPUT: 

result: 1
result: 11
result: 1989
result: VOD
.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

'''