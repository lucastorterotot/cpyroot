from ROOT import TH1F, THStack

class TreeStack(object):

    def __init__(self, name):
        self.name = name
        self.trees = dict()
        self.treenames = []
        self.hists = []
        self.histsum = None
        self.stack = THStack('_'.join([self.name, 'stack']),
                             'title')

    def add(self, name, tree):
        self.trees[name] = tree
        self.treenames.append(name)

    def hname(self, name):
        return '_'.join([self.name, name])
        
    def project(self, var, cut, bins, xmin, xmax):
        for name in self.treenames:
            tree = self.trees[name]
            hname = self.hname(name)
            self.hists.append(TH1F(hname, hname, bins, xmin, xmax))
            tree.Project(hname, var, cut)
        for hist in self.hists:
            if self.histsum is None:
                self.histsum = hist.Clone(self.hname('sum'))
            else:
                self.histsum.Add(hist)
            self.stack.Add(hist)
            
    def draw(self):
        self.stack.Draw()
        self.histsum.Draw('same')
