#!/usr/bin/env python
import sys

if len(sys.argv) != 5:
    print 'usage: shorten_tree.py <tree_name> <input root file> <output root file> <nevents>'
    sys.exit(1)
tname, ifile, ofile, nevents = sys.argv[1:]
nevents = int(nevents)

from ROOT import TFile
import sys

ifile = TFile(ifile)
itree = ifile.Get(tname)
rofile = TFile(ofile, 'recreate')
print nevents
otree = itree.CloneTree(nevents)
otree.Write()
rofile.Close()


