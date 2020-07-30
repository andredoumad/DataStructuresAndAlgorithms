# Andre Doumad

# Breadth first search graph

import unittest

class Graph(object):
    def __init__(self, v):
        print('initialize')
        self.v = v
        self.adj = {}
        for i in range(0, v):
            self.adj[i] = [i]
        for key, value in self.adj.items():
            print('key: ' + str(key) + ' val is ' + str(value))

    def addEdge(self, v, w):
        print('addEdge')
        if v in self.adj:
            self.adj[v].append(w)
        for key, value in self.adj.items():
            print('key: ' + str(key) + ' val is ' + str(value))

    def bfs(self, s):
        print('breadth first search')
        b_visited = {}
        queue = []
        b_visited[s] = True
        print('starting at ' + str(s))
        queue.append(s)

        while len(queue) > 0:
            s = queue.pop()
            # print('deque ' + str(s))
            while len(self.adj[s]) > 0:

                n = self.adj[s].pop()
                if n not in b_visited:
                    b_visited[n] = True
                    # print('queuing ' + str(n))
                    print('node ' + str(s) +  ' is connected to ' + str(n))
                    queue.append(n)

            del self.adj[s]


# unittest
class unitTest(unittest.TestCase):

    def test_a(self):
        g = Graph(8)
        g.addEdge(0, 1)
        g.addEdge(1, 0)
        g.addEdge(1, 4)
        g.addEdge(4, 1)
        g.addEdge(4, 6)
        g.addEdge(6, 4)
        g.addEdge(6, 0)
        g.addEdge(0, 6)
        g.addEdge(1, 5)
        g.addEdge(5, 1)
        g.addEdge(5, 3)
        g.addEdge(3, 5)
        g.addEdge(3, 0)
        g.addEdge(0, 3)
        g.addEdge(5, 2)
        g.addEdge(2, 5)
        g.addEdge(2, 7)
        g.addEdge(7, 2)

        print("Breadth First Traversal")

        g.bfs(0)


if __name__ == '__main__':
    unittest.main()

'''
OUTPUT:

initialize
key: 0 val is [0]
key: 1 val is [1]
key: 2 val is [2]
key: 3 val is [3]
key: 4 val is [4]
key: 5 val is [5]
key: 6 val is [6]
key: 7 val is [7]
addEdge
key: 0 val is [0, 1]
key: 1 val is [1]
key: 2 val is [2]
key: 3 val is [3]
key: 4 val is [4]
key: 5 val is [5]
key: 6 val is [6]
key: 7 val is [7]
addEdge
key: 0 val is [0, 1]
key: 1 val is [1, 0]
key: 2 val is [2]
key: 3 val is [3]
key: 4 val is [4]
key: 5 val is [5]
key: 6 val is [6]
key: 7 val is [7]
addEdge
key: 0 val is [0, 1]
key: 1 val is [1, 0, 4]
key: 2 val is [2]
key: 3 val is [3]
key: 4 val is [4]
key: 5 val is [5]
key: 6 val is [6]
key: 7 val is [7]
addEdge
key: 0 val is [0, 1]
key: 1 val is [1, 0, 4]
key: 2 val is [2]
key: 3 val is [3]
key: 4 val is [4, 1]
key: 5 val is [5]
key: 6 val is [6]
key: 7 val is [7]
addEdge
key: 0 val is [0, 1]
key: 1 val is [1, 0, 4]
key: 2 val is [2]
key: 3 val is [3]
key: 4 val is [4, 1, 6]
key: 5 val is [5]
key: 6 val is [6]
key: 7 val is [7]
addEdge
key: 0 val is [0, 1]
key: 1 val is [1, 0, 4]
key: 2 val is [2]
key: 3 val is [3]
key: 4 val is [4, 1, 6]
key: 5 val is [5]
key: 6 val is [6, 4]
key: 7 val is [7]
addEdge
key: 0 val is [0, 1]
key: 1 val is [1, 0, 4]
key: 2 val is [2]
key: 3 val is [3]
key: 4 val is [4, 1, 6]
key: 5 val is [5]
key: 6 val is [6, 4, 0]
key: 7 val is [7]
addEdge
key: 0 val is [0, 1, 6]
key: 1 val is [1, 0, 4]
key: 2 val is [2]
key: 3 val is [3]
key: 4 val is [4, 1, 6]
key: 5 val is [5]
key: 6 val is [6, 4, 0]
key: 7 val is [7]
addEdge
key: 0 val is [0, 1, 6]
key: 1 val is [1, 0, 4, 5]
key: 2 val is [2]
key: 3 val is [3]
key: 4 val is [4, 1, 6]
key: 5 val is [5]
key: 6 val is [6, 4, 0]
key: 7 val is [7]
addEdge
key: 0 val is [0, 1, 6]
key: 1 val is [1, 0, 4, 5]
key: 2 val is [2]
key: 3 val is [3]
key: 4 val is [4, 1, 6]
key: 5 val is [5, 1]
key: 6 val is [6, 4, 0]
key: 7 val is [7]
addEdge
key: 0 val is [0, 1, 6]
key: 1 val is [1, 0, 4, 5]
key: 2 val is [2]
key: 3 val is [3]
key: 4 val is [4, 1, 6]
key: 5 val is [5, 1, 3]
key: 6 val is [6, 4, 0]
key: 7 val is [7]
addEdge
key: 0 val is [0, 1, 6]
key: 1 val is [1, 0, 4, 5]
key: 2 val is [2]
key: 3 val is [3, 5]
key: 4 val is [4, 1, 6]
key: 5 val is [5, 1, 3]
key: 6 val is [6, 4, 0]
key: 7 val is [7]
addEdge
key: 0 val is [0, 1, 6]
key: 1 val is [1, 0, 4, 5]
key: 2 val is [2]
key: 3 val is [3, 5, 0]
key: 4 val is [4, 1, 6]
key: 5 val is [5, 1, 3]
key: 6 val is [6, 4, 0]
key: 7 val is [7]
addEdge
key: 0 val is [0, 1, 6, 3]
key: 1 val is [1, 0, 4, 5]
key: 2 val is [2]
key: 3 val is [3, 5, 0]
key: 4 val is [4, 1, 6]
key: 5 val is [5, 1, 3]
key: 6 val is [6, 4, 0]
key: 7 val is [7]
addEdge
key: 0 val is [0, 1, 6, 3]
key: 1 val is [1, 0, 4, 5]
key: 2 val is [2]
key: 3 val is [3, 5, 0]
key: 4 val is [4, 1, 6]
key: 5 val is [5, 1, 3, 2]
key: 6 val is [6, 4, 0]
key: 7 val is [7]
addEdge
key: 0 val is [0, 1, 6, 3]
key: 1 val is [1, 0, 4, 5]
key: 2 val is [2, 5]
key: 3 val is [3, 5, 0]
key: 4 val is [4, 1, 6]
key: 5 val is [5, 1, 3, 2]
key: 6 val is [6, 4, 0]
key: 7 val is [7]
addEdge
key: 0 val is [0, 1, 6, 3]
key: 1 val is [1, 0, 4, 5]
key: 2 val is [2, 5, 7]
key: 3 val is [3, 5, 0]
key: 4 val is [4, 1, 6]
key: 5 val is [5, 1, 3, 2]
key: 6 val is [6, 4, 0]
key: 7 val is [7]
addEdge
key: 0 val is [0, 1, 6, 3]
key: 1 val is [1, 0, 4, 5]
key: 2 val is [2, 5, 7]
key: 3 val is [3, 5, 0]
key: 4 val is [4, 1, 6]
key: 5 val is [5, 1, 3, 2]
key: 6 val is [6, 4, 0]
key: 7 val is [7, 2]
Breadth First Traversal
breadth first search
starting at 0
node 0 is connected to 3
node 0 is connected to 6
node 0 is connected to 1
node 1 is connected to 5
node 1 is connected to 4
node 5 is connected to 2
node 2 is connected to 7
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK

'''