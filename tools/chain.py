import glob

print 'importing Chain'

from ROOT import TChain, TFile, TTree

class Chain( object ):
    '''
    TChain with file auto-loading. Use just like a TChain.
    '''
    def __init__(self, pattern, treeName=None):
        '''
        pattern:  pattern for files, e.g. "*.root"
        treeName: name of the trees in your files. if not provided, 
                  attempt to guess the name of your tree.
        '''
        self.files = []
        if treeName is None:
            treeName = self.guessTreeName(pattern)
        self.chain = TChain(treeName)
        nFiles = 0
        for file in glob.glob(pattern):
            self.chain.Add(file)
            nFiles += 1
        if nFiles==0:
            raise ValueError('no matching file name: '+pattern)

    def guessTreeName(self, pattern):
        names = []
        for fnam in glob.glob(pattern):
            rfile = TFile(fnam)
            for key in rfile.GetListOfKeys():
                obj = rfile.Get(key.GetName())
                if type(obj) is TTree:
                    names.append( key.GetName() )
        thename = set(names)
        if len(thename)==1:
            return list(thename)[0]


    def __getattr__(self, attr):
        return getattr(self.chain, attr)

