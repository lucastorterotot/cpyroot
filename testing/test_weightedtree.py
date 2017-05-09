import unittest
from cpyroot.tools.weightedtree import WeightedTree
from testtree import create_tree
from ROOT import TFile, TH1F

class WeightedTreeTestCase(unittest.TestCase):
    
    def setUp(self):
        self.tfile = TFile( create_tree() ) 
        self.ttree = self.tfile.Get('test_tree') 
    
    def tearDown(self):
        self.tfile.Close()
    
    def test_create(self):
        '''Test simple creation and inheritance'''
        tree = WeightedTree(self.ttree)
        self.assertEqual(tree.GetEntries(), 200)
        
    def test_cut_str(self):
        h_from = TH1F('h1', 'h1', 2, 0, 200)
        h_from.SetBinContent(1, 1)
        h_from.SetBinContent(2, 1)
        h_to = TH1F('h_to', 'h_to', 2, 0, 200)
        h_to.SetBinContent(0, 0)
        h_to.SetBinContent(2, 1)
        wtree = WeightedTree(self.ttree)
        wtree.set_weight('iev', h_from, h_to)
        weightstr = wtree.weight_str_from_hist()
        self.assertEqual('(iev>=0.0 && iev<100.0)*0.0 + (iev>=100.0 && iev<200.0)*1.0',
                         weightstr)
        
if __name__ == '__main__':
    unittest.main()
    
