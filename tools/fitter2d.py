from ROOT import gDirectory, TH2F, TH1F, TFile

class Fitter2D(object):

    def __init__(self, *args):
        self.h2d = TH2F(*args)
    
    def draw2D(self, *args):
        self.h2d.Draw(*args)
        self.hmean.Draw('psame')

    def fit(self, bin, opt='0'): 
        hslice = self.h2d.ProjectionY("", bin, bin, "")
        if not hslice.GetEntries(): 
            return 0., 0., 0., 0., 0., 0.
        hslice.Fit('gaus', opt)
        func = hslice.GetFunction('gaus')
        x = self.h2d.GetXaxis().GetBinCenter(bin)
        dx = self.h2d.GetXaxis().GetBinWidth(bin)
        mean = func.GetParameter(1)
        dmean = func.GetParError(1)
        sigma = func.GetParameter(2)
        dsigma = func.GetParError(2)
        return x, dx, mean, dmean, sigma, dsigma

    def fit_slices(self):
        self.h2d.FitSlicesY()
        self.hmean = gDirectory.Get( self.h2d.GetName() + '_1' )
        self.hsigma = gDirectory.Get( self.h2d.GetName() + '_2' )
        # self.hsigma.SetYTitle('#sigma(MET_{x,y})')
        self.hchi2 = gDirectory.Get( self.h2d.GetName() + '_chi2' )

    def format(self, style, xtitle):
        for hist in [self.hmean, self.hsigma, self.hchi2]: 
            style.format(hist)
            hist.SetTitle('')
            hist.SetXTitle(xtitle)

    def write(self):
        outfile = TFile(self.h2d.GetName()+'.root', 'recreate')
        for hist in [self.hmean, self.hsigma, self.hchi2, self.h2d]: 
            hist.Clone()
            hist.SetDirectory(outfile)
        outfile.Write()
        outfile.Close()
        
