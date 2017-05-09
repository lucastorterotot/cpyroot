import unittest
from cpyroot import * 
import cpyroot.tools.DataMC as DataMC
from ROOT import TFile, TH1F

file1 = 'test1.root'
file2 = 'test2.root'

class DataMCTestCase(unittest.TestCase):
    
    def setUp(self):
        self.t1 = Chain(file1)
        self.t2 = Chain(file2)
        
    def test_1(self):
        pass
    
        
if __name__ == '__main__':
    from testtree import create_tree    
    import os
    if not os.path.isfile(file1):
        create_tree(file1, 0, 1, 5000)
    if not os.path.isfile(file2):
        create_tree(file2, 1, 0.2, 5000)
    unittest.main()        
