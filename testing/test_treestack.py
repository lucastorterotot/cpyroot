import unittest
from cpyroot import *
from testtree import create_tree
import time

file1 = 'test1.root'
file2 = 'test2.root'

class TreeStackTestCase(unittest.TestCase):

    def setUp(self):
        self.t1 = Chain(file1)
        self.t2 = Chain(file2)
        
    def test_1(self):
        self.assertTrue(self.t1)
        self.assertTrue(self.t2)
        stack = TreeStack('MyStack')
        stack.add('bulk', self.t1)
        stack.add('peak', self.t2)
        stack.project('x','1', 100, -5, 5)
        stack.draw()
        gPad.Update()
        time.sleep(5)
        # stack.histsum.Draw()
        # gPad.Update()
        # time.sleep(1)
        

if __name__ == '__main__':
    import os
    if not os.path.isfile(file1):
        create_tree(file1, 0, 1, 5000)
    if not os.path.isfile(file2):
        create_tree(file2, 1, 0.2, 5000)
    unittest.main()        
