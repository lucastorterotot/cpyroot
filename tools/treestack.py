from ROOT import TH1F, THStack

class TreeStack(object):

    def __init__(self, name):
        '''Name is the name you want for your treestack.'''
        self.name = name
        self.trees = dict()
        self.styles = dict()
        self.treenames = []
        self.hists = []
        self.histsum = None
        self.stack = THStack('_'.join([self.name, 'stack']),
                             'title')

    def add(self, name, tree, style=None):
        '''Add a new tree with name "name".
        
        Your tree should have the method Project.
        You may implement tree weighting in this function.

        style should behave like in tools.style
        '''
        self.trees[name] = tree
        self.styles[name] = style
        self.treenames.append(name)

    def hname(self, name):
        return '_'.join([self.name, name])
        
    def project(self, var, cut, bins, xmin, xmax):
        '''Fill the histograms with all trees, 
        using: 
        var : variable to plot
        cut : cut to use
        These variables will be passed to the Project method of your trees. 
        bins, xmin, xmax defins the histogram binning.
        '''
        for name in self.treenames:
            tree = self.trees[name]
            hname = self.hname(name)
            hist = TH1F(hname, hname, bins, xmin, xmax)
            self.hists.append(hist)
            self.styles[name].formatHisto(hist)
            tree.Project(hname, var, cut)
        for hist in self.hists:
            if self.histsum is None:
                self.histsum = hist.Clone(self.hname('sum'))
            else:
                self.histsum.Add(hist)
            self.stack.Add(hist)
            
    def draw(self):
        '''Draw the stack. Call project first.'''
        self.stack.Draw()
        # self.histsum.Draw('same')
