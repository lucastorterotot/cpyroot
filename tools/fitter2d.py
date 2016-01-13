class Fitter2D(object):
    
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
