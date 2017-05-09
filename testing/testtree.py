from ROOT import TFile
from cpyroot import *
import random

FNAME="test_tree.root"

def create_tree(filename=FNAME, mean=0, sigma=1, nentries=None):
    '''Create the test tree in file FNAME.'''
    if not nentries: 
        if os.path.isfile(filename):
            #default number of entries, file exists
            return filename
        else: 
            nentries = 200
    nentries = int(nentries)
    outfile = TFile(filename, 'recreate')
    tree = Tree('test_tree', 'A test tree')
    tree.var('x')
    tree.var('iev')
    for i in range(nentries):
        tree.fill('x', random.gauss(mean, sigma))        
        tree.fill('iev', i)
        tree.tree.Fill()
    outfile.Write()
    outfile.Close()
    return outfile.GetName()

def remove_tree(filename=FNAME):
    '''Remove the test tree.'''
    os.remove(filename)

if __name__ == '__main__':
    create_tree()
