from ROOT import TFile
from cpyroot import *
import random

def create_tree(filename="test_tree.root", mean=0, sigma=1, nevents=5000): 
    outfile = TFile(filename, 'recreate')
    tree = Tree('test_tree', 'A test tree')
    tree.var('x')
    for i in range(nevents):
        tree.fill('x', random.gauss(mean, sigma))
        tree.tree.Fill()
    print 'creating a tree', tree.tree.GetName(),\
        tree.tree.GetEntries(), 'entries in',\
        outfile.GetName()
    outfile.Write()

if __name__ == '__main__':
    create_tree()
