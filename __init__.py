import os
import sys
import fnmatch
import ROOT


from ROOT import gROOT, TFile, TCanvas, TPad, gPad, TBrowser, TH2F, TH1F, TH1D , TProfile, THStack, TLegend, gDirectory, gStyle, TF1, TEventList, TGraphErrors
from ROOT import kRed, kGray, kWhite, kBlue, kGreen, kYellow


from tools.chain import Chain
from tools.histcomparator import HistComparator
from tools.tree import Tree
from tools.treestack import TreeStack
from tools.style import *
from tools.officialstyle import * 

gROOT.Macro( os.path.expanduser( '~/rootlogon.C' ) )

# adding current directory in PYTHONPATH
sys.path.append('.')

filename = os.environ.get('PYTHONSTARTUP')
if filename and os.path.isfile(filename):
    exec(open(filename).read())

canvases = []
cx = 500
cy = 500

histTypes = [ ROOT.TH1F,
              ROOT.TH1D,
              ROOT.TH2F,
              ROOT.TH2D,
              ROOT.TProfile ]

dirTypes = [ROOT.TDirectory, ROOT.TDirectoryFile]

hists = None
trees = None
dirs = None
current_file = None


def ls():
    if gDirectory is None:
        print 'No current directory... open a root file?'
    else:
        gDirectory.ls()

def start_message():
    print
    print 
    print '-'*30, 'CPYROOT', '-'*30
    print
    print '''
    The most used ROOT classes are available. 
    If some are missing, just do:
       from ROOT import <the root class you want>
    to autoload histograms and trees from a root file, do
       load(<file.root>, locals())
    '''

start_message()
    
class Directory(object):
    '''Like TDirectory, but autoloads directory contents'''
    def __init__(self, tdir):
        self.tdir = tdir
    def __getattr__(self, attr):
        return getattr(self.tdir, attr)
    def cd(self, theLOCALS=None):
        if theLOCALS is None:
            theLOCALS = LOCALS
        self.tdir.cd()
        hists = load(theLOCALS, self, histTypes)
        trees = load(theLOCALS, self, [ROOT.TTree])
        dirs = load(theLOCALS, self, dirTypes)

def draw(pattern):
    '''Draw all histograms with a key matching pattern in separate canvases'''
    for hist in hists:
        name = hist.GetName()
        if fnmatch.fnmatch(name, pattern):
            can =  TCanvas(name, name, cx, cy)
            canvases.append( can )
            can.Draw()
            hist.Draw()

def _load(locals, dir, types):
    '''Load objects in dir with a type in types.'''
    objs = []
    for key in dir.GetListOfKeys():
        obj = dir.Get(key.GetName())
        if type(obj) in types:
            print 'loading', type(obj), key.GetName()
            if type(obj) in dirTypes:
                obj = Directory(obj)
            objs.append(obj)
            locals[key.GetName()] = obj
    return objs


def load(filename, caller_vars):
    global current_file
    current_file = TFile(filename)
    hists = _load(caller_vars, current_file, histTypes)
    trees = _load(caller_vars, current_file, [ROOT.TTree])
    dirs = _load(caller_vars, current_file, dirTypes)

# def treeComp(t1, t2, var, cut):
#     t1.SetWeight(1./t1.GetEntries(), 'global')
#     t2.SetWeight(1./t2.GetEntries(), 'global')
#     t1.Draw(var, cut)
#     t2.Draw(var, cut, 'same')
