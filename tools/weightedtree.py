from ROOT import TTree, TCanvas, TLegend

class WeightedTree(object):
    
    def __init__(self, tree):
        self.tree = tree
              
    def __getattr__(self, attr):
        return getattr(self.tree, attr)
        
    def set_weight(self, var, h_from, h_to):
        '''set up the weights.
        
        parameters:
         - var is the tree variable that will be used for weighting
         - h_from is the original distribution for this variable
         - h_to is the desired distribution
        '''
        self.var = var
        self.h_from = h_from
        self.h_to = h_to
        self.h_from.SetMarkerStyle(8)
        self.h_to.SetMarkerStyle(21)
        self.h_to.SetMarkerColor(4)
        self.h_weight = h_to.Clone('h_weight')
        self.h_weight.Divide(h_from)
        self.weigth_str = self.weight_str_from_hist()
        for h in [self.h_from, self.h_to, self.h_weight]:
            h.SetStats(False)
            h.SetXTitle('p_{T}^{gen} (GeV)')
         
    def weight_str_from_hist(self, hist=None):
        if not hist:
            hist = self.h_weight
        strs = []
        for ibin in range(1, hist.GetNbinsX() + 1):
            bin_str = '({var}>={themin} && {var}<{themax})*{weight}'.format(
                var=self.var,
                themin=hist.GetXaxis().GetBinLowEdge(ibin),
                themax=hist.GetXaxis().GetBinUpEdge(ibin),
                weight=hist.GetBinContent(ibin)
            )
            strs.append(bin_str)
        return ' + '.join(strs)
            
    def Draw(self, *args):
        args = list(args)
        assert(len(args)>0)
        if len(args) == 1:
            args.append('1')
        cut = args[1]
        wcut = '({})*({})'.format(cut, self.weigth_str)
        largs = list(args)
        largs[1] = wcut
        args = tuple(largs)
        # print args
        self.tree.Draw(*args)
        
    def plot(self):
        self.c1 = TCanvas('c1', '')
        first, second = self.h_from, self.h_to
        if first.GetMaximum()<second.GetMaximum():
            first, second = second, first
        first.Draw()
        second.Draw('same')
        self.legend_c1 = TLegend(0.6,0.7, 0.85, 0.85)
        self.legend_c1.AddEntry(self.h_from, self.h_from.GetTitle())
        self.legend_c1.AddEntry(self.h_to, self.h_to.GetTitle())
        self.legend_c1.Draw()      
        self.c2 = TCanvas('c2', '')
        self.h_weight.Draw()
    
    
