# Andre Doumad

import unittest, time
# fibonacci
class Fibonacci(object):
    def memoize(self, func):
        cache = dict()
        def mem_func(self, *args):
            if args in cache:
                return args
            result = func(self, *args)
            cache[args] = result
            return result

        return mem_func

    def fib(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)

# unittest
class unitTest(unittest.TestCase):
    def test_0(self):

        fib = Fibonacci()
        memFib = fib.memoize(fib.fib)
        startTime = time.time()
        memFib(35)
        print('execution time: ' + str(time.time()-startTime))
        startTime = time.time()
        memFib(35)
        print('execution time: ' + str(time.time()-startTime))
if __name__ == '__main__':
    unittest.main()

'''
OUTPUT:

execution time: 2.7108664512634277
execution time: 1.9073486328125e-06
.
----------------------------------------------------------------------
Ran 1 test in 2.711s

OK

'''