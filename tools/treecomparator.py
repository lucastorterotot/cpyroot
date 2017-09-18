from cpyroot.tools.style import * 
from cpyroot.tools.histcomparator import * 

num = 0
def hname():
    global num
    num+=1
    return 'h_{num}'.format(num=num)

legend = None

########################################################################
class TreeComparator(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, t1, t2, 
                 name1=None, name2=None,
                 w1='1', w2='1',
                 normalize=None):  
        """Constructor"""
        if name1 is None: name1 = t1.GetTitle()
        if name2 is None: name2 = t2.GetTitle()        
        self.name1 = name1
        self.name2 = name2
        self.t1 = t1
        self.t2 = t2
        self.w1 = w1
        self.w2 = w2
        self.normalize = normalize
        self.legend = None
        self.h1 = None
        self.h2 = None
        self.comparator = None
        
    def draw(self, var, cut='1',
             nbins=100, xmin=0, xmax=200):
        self.h1 = TH1F(hname(), '', nbins, xmin, xmax)
        self.h1.Sumw2()
        self.t1.Project(self.h1.GetName(), var,'({cut})*({w1})'.format(cut=cut,w1=self.w1),'')
        self.h2 = self.h1.Clone(hname())
        self.h2.Sumw2()
        self.t2.Project(self.h2.GetName(), var,'({cut})*({w2})'.format(cut=cut,w2=self.w2),'')
        if self.normalize == None:
            pass
        elif self.normalize == -1:
            self.h1.Scale(1./self.h1.Integral())
            self.h2.Scale(1./self.h2.Integral())
        elif self.normalize>0:
            self.h2.Scale( self.normalize )
        sBlue.markerStyle = 25
        sBlue.formatHisto(self.h2)
        sBlack.formatHisto(self.h1)
        self.h2.SetFillStyle(1001)
        self.h2.SetFillColor(5)
        self.h1.SetMarkerSize(0.8)
        self.h2.SetMarkerSize(0.8)
        self.h1.SetStats(0)
        self.h2.SetStats(0)
        if self.name1 is None: self.name1 = self.t1.GetTitle()
        if self.name2 is None: self.name2 = self.t2.GetTitle()
        self.h1.SetTitle(self.name1)
        self.h2.SetTitle(self.name2)
        self.legend = TLegend(0.55,0.7,0.88,0.88)
        self.legend.SetFillColor(0)
        self.legend.AddEntry(self.h1, self.name1, 'lp')
        self.legend.AddEntry(self.h2, self.name2, 'lpf')
    
        print 'number of selected rows:', self.t1.GetSelectedRows(), self.t2.GetSelectedRows()
    
        self.comparator = HistComparator(var, self.h1, self.h2)
        self.comparator.draw()
    
##
##def draw(var1=None, cut=1,
##         t1=None, t2=None, w1='1', w2='1',
##         name1=None, name2=None,
##         normalize=None,
##         nbins=20, xmin=0, xmax=200, var2=None):
##    '''Comparison plot for var1.
##    
##    cut : cut to be applied
##    t1 and t2 : the 2 trees to be compared
##    w1 and w2 : weights for the two trees
##    nbins,min,max : histogram binning
##    '''
##    if var2 is None:
##        var2 = var1
##    if t1 is None or t2 is None:
##        raise ValueError('please provide the 2 trees, t1 and t2.')
##    print 'tree1',
##    print '\t var   : ' , var1
##    print '\t weight:', w1
##    print 'tree2',
##    print '\t var   : ' , var2
##    print '\t weight:', w2
##    print 'cut', cut
##    global legend
##    h1 = TH1F(hname(), '', nbins, xmin, xmax)
##    h1.Sumw2()
##    t1.Project(h1.GetName(), var1,'({cut})*({w1})'.format(cut=cut,w1=w1),'')
##    h2 = h1.Clone(hname())
##    h2.Sumw2()
##    t2.Project(h2.GetName(), var2,'({cut})*({w2})'.format(cut=cut,w2=w2),'')
##    if normalize == None:
##        pass
##    elif normalize == -1:
##        h1.Scale(1./h1.Integral())
##        h2.Scale(1./h2.Integral())
##    elif normalize>0:
##        h2.Scale( normalize )
##    sBlue.markerStyle = 25
##    sBlue.formatHisto(h2)
##    sBlack.formatHisto(h1)
##    h2.SetFillStyle(1001)
##    h2.SetFillColor(5)
##    h1.SetMarkerSize(0.8)
##    h2.SetMarkerSize(0.8)
##    h1.SetStats(0)
##    h2.SetStats(0)
##    if name1 is None: name1 = t1.GetTitle()
##    if name2 is None: name2 = t2.GetTitle()
##    h1.SetTitle(name1)
##    h2.SetTitle(name2)
##    legend = TLegend(0.55,0.7,0.88,0.88)
##    legend.SetFillColor(0)
##    legend.AddEntry(h1, name1, 'lp')
##    legend.AddEntry(h2, name2, 'lpf')
##
##    print 'number of selected rows:', t1.GetSelectedRows(), t2.GetSelectedRows()
##
##    comparator = HistComparator(var1, h1, h2)
##    comparator.draw()
##    return comparator
##
##
##def simpleDraw(var, cut='1'):
##    if len(trees)!=2:
##        print 'this function cannot be used if you have a number of trees different than 2 in the "trees" dictionary.'
##        return
##
##    t1 = None
##    t2 = None
##    name1 = None
##    name2 = None
##    for index, (alias, tree) in enumerate(sorted(trees.iteritems())):
##        if index==0:
##            t1 = tree
##            name1 = alias
##        else:
##            t2 = tree
##            name2 = alias
##
##    return draw(var1=var, cut=cut, t1=t1, t2=t2, name1=name1, name2=name2)
##    
##
##trees = None
##
##def getTrees( treeName, patterns ):
##    trees = dict()
##    for alias, pattern in patterns:
##        print 'loading', alias, treeName, pattern
##        tree = Chain(treeName, pattern)
##        tmpalias = alias
##        num=0
##        while tmpalias in trees:
##            num += 1
##            tmpalias = '{alias}_{num}'.format(alias=alias, num=num)
##        trees[tmpalias] = tree
##        # tree.SetWeight(1./tree.GetEntries(), 'global')
##    return trees
##
##def main():
##    import sys
##    import pprint
##    from optparse import OptionParser
##    
##    parser = OptionParser()
##    
##    parser.usage = """
##    %prog -i <tree_alias:root_file_name> <tree_alias:root_file_name>
##
##    if you do not provide the var option, you can e.g. do:
##    comp = draw('jet2_eta', 'jet2_pt>30', trees[a1], trees[a2], name1=a1, name2=a2, xmin=-5, xmax=5); comp.draw()
##    """
##    parser.add_option("-v", "--var", 
##                      dest="var", 
##                      help="variable to draw.",
##                      default=None)
##    parser.add_option("-c", "--cut", 
##                      dest="cut", 
##                      help="cut to apply",
##                      default='1')
##    parser.add_option("-o", "--outdir", 
##                      dest="outdir", 
##                      help="output director for plots",
##                      default='Comparator_OutDir')
##    parser.add_option("-t", "--tree", 
##                      dest="tree", 
##                      help="name of tree in files",
##                      default=None)
##
##    (options,args) = parser.parse_args()
##
##    if len(args)!=2:
##        parser.print_usage()
##        sys.exit(1)
##    
##    a1,p1 = args[0].split(':')
##    a2,p2 = args[1].split(':')
##    patterns = [ (a1, p1), (a2, p2) ]
##    trees = getTrees( options.tree, patterns)
##    pprint.pprint(trees)
##
##    comp = None
##    if options.var:
##        comp = draw(options.var, options.cut,
##                    trees[a1], trees[a2],
##                    name1=a1, name2=a2);
##        comp.draw()
##        
##    return trees, a1, a2, options
##
##if __name__ == '__main__':
##    trees, a1, a2, options = main() 
