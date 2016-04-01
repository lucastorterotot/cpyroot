from ROOT import kBlack, TLatex, TCanvas, TPad, gStyle, TStyle, kWhite
import copy

def setTDRStyle():
  tdrStyle =  TStyle("tdrStyle","Style for P-TDR")

   #for the canvas:
  tdrStyle.SetCanvasBorderMode(0)
  tdrStyle.SetCanvasColor(kWhite)
  tdrStyle.SetCanvasDefH(600) #Height of canvas
  tdrStyle.SetCanvasDefW(600) #Width of canvas
  tdrStyle.SetCanvasDefX(0)   #POsition on screen
  tdrStyle.SetCanvasDefY(0)


  tdrStyle.SetPadBorderMode(0)
  #tdrStyle.SetPadBorderSize(Width_t size = 1)
  tdrStyle.SetPadColor(kWhite)
  tdrStyle.SetPadGridX(False)
  tdrStyle.SetPadGridY(False)
  tdrStyle.SetGridColor(0)
  tdrStyle.SetGridStyle(3)
  tdrStyle.SetGridWidth(1)

#For the frame:
  tdrStyle.SetFrameBorderMode(0)
  tdrStyle.SetFrameBorderSize(1)
  tdrStyle.SetFrameFillColor(0)
  tdrStyle.SetFrameFillStyle(0)
  tdrStyle.SetFrameLineColor(1)
  tdrStyle.SetFrameLineStyle(1)
  tdrStyle.SetFrameLineWidth(1)
  
#For the histo:
  #tdrStyle.SetHistFillColor(1)
  #tdrStyle.SetHistFillStyle(0)
  tdrStyle.SetHistLineColor(1)
  tdrStyle.SetHistLineStyle(0)
  tdrStyle.SetHistLineWidth(1)
  #tdrStyle.SetLegoInnerR(Float_t rad = 0.5)
  #tdrStyle.SetNumberContours(Int_t number = 20)

  tdrStyle.SetEndErrorSize(2)
  #tdrStyle.SetErrorMarker(20)
  #tdrStyle.SetErrorX(0.)
  
  tdrStyle.SetMarkerStyle(20)
  
#For the fit/function:
  tdrStyle.SetOptFit(1)
  tdrStyle.SetFitFormat("5.4g")
  tdrStyle.SetFuncColor(2)
  tdrStyle.SetFuncStyle(1)
  tdrStyle.SetFuncWidth(1)

#For the date:
  tdrStyle.SetOptDate(0)
  # tdrStyle.SetDateX(Float_t x = 0.01)
  # tdrStyle.SetDateY(Float_t y = 0.01)

# For the statistics box:
  tdrStyle.SetOptFile(0)
  tdrStyle.SetOptStat(0) # To display the mean and RMS:   SetOptStat("mr")
  tdrStyle.SetStatColor(kWhite)
  tdrStyle.SetStatFont(42)
  tdrStyle.SetStatFontSize(0.025)
  tdrStyle.SetStatTextColor(1)
  tdrStyle.SetStatFormat("6.4g")
  tdrStyle.SetStatBorderSize(1)
  tdrStyle.SetStatH(0.1)
  tdrStyle.SetStatW(0.15)
  # tdrStyle.SetStatStyle(Style_t style = 1001)
  # tdrStyle.SetStatX(Float_t x = 0)
  # tdrStyle.SetStatY(Float_t y = 0)

# Margins:
  tdrStyle.SetPadTopMargin(0.05)
  tdrStyle.SetPadBottomMargin(0.13)
  tdrStyle.SetPadLeftMargin(0.16)
  tdrStyle.SetPadRightMargin(0.02)

# For the Global title:

  tdrStyle.SetOptTitle(0)
  tdrStyle.SetTitleFont(42)
  tdrStyle.SetTitleColor(1)
  tdrStyle.SetTitleTextColor(1)
  tdrStyle.SetTitleFillColor(10)
  tdrStyle.SetTitleFontSize(0.05)
  # tdrStyle.SetTitleH(0) # Set the height of the title box
  # tdrStyle.SetTitleW(0) # Set the width of the title box
  # tdrStyle.SetTitleX(0) # Set the position of the title box
  # tdrStyle.SetTitleY(0.985) # Set the position of the title box
  # tdrStyle.SetTitleStyle(Style_t style = 1001)
  # tdrStyle.SetTitleBorderSize(2)

# For the axis titles:

  tdrStyle.SetTitleColor(1, "XYZ")
  tdrStyle.SetTitleFont(42, "XYZ")
  tdrStyle.SetTitleSize(0.06, "XYZ")
  # tdrStyle.SetTitleXSize(Float_t size = 0.02) # Another way to set the size?
  # tdrStyle.SetTitleYSize(Float_t size = 0.02)
  tdrStyle.SetTitleXOffset(0.9)
  tdrStyle.SetTitleYOffset(1.25)
  # tdrStyle.SetTitleOffset(1.1, "Y") # Another way to set the Offset

# For the axis labels:

  tdrStyle.SetLabelColor(1, "XYZ")
  tdrStyle.SetLabelFont(42, "XYZ")
  tdrStyle.SetLabelOffset(0.007, "XYZ")
  tdrStyle.SetLabelSize(0.05, "XYZ")

# For the axis:

  tdrStyle.SetAxisColor(1, "XYZ")
  tdrStyle.SetStripDecimals(True)
  tdrStyle.SetTickLength(0.03, "XYZ")
  tdrStyle.SetNdivisions(510, "XYZ")
  tdrStyle.SetPadTickX(1)  # To get tick marks on the opposite side of the frame
  tdrStyle.SetPadTickY(1)

# Change for log plots:
  tdrStyle.SetOptLogx(0)
  tdrStyle.SetOptLogy(0)
  tdrStyle.SetOptLogz(0)

# Postscript options:
  tdrStyle.SetPaperSize(20.,20.)
  # tdrStyle.SetLineScalePS(Float_t scale = 3)
  # tdrStyle.SetLineStyleString(Int_t i, const char* text)
  # tdrStyle.SetHeaderPS(const char* header)
  # tdrStyle.SetTitlePS(const char* pstitle)

  # tdrStyle.SetBarOffset(Float_t baroff = 0.5)
  # tdrStyle.SetBarWidth(Float_t barwidth = 0.5)
  # tdrStyle.SetPaintTextFormat(const char* format = "g")
  # tdrStyle.SetPalette(Int_t ncolors = 0, Int_t* colors = 0)
  # tdrStyle.SetTimeOffset(Double_t toffset)
  # tdrStyle.SetHistMinimumZero(kTRUE)

  tdrStyle.SetHatchesLineWidth(5)
  tdrStyle.SetHatchesSpacing(0.05)

  tdrStyle.cd()


  
def officialStyle(style):
    style =  TStyle("tdrStyle","Style for P-TDR")

    style.SetCanvasColor (0)
    style.SetCanvasBorderSize(10)
    style.SetCanvasBorderMode(0)
    style.SetCanvasDefH (700)
    style.SetCanvasDefW (700)
    style.SetCanvasDefX (100)
    style.SetCanvasDefY (100)
    # color palette for 2D temperature plots
    # style.SetPalette(1,0)
    # Pads
    style.SetPadColor (0)
    style.SetPadBorderSize (10)
    style.SetPadBorderMode (0)
    
    style.SetPadBottomMargin(0.15)
    style.SetPadTopMargin (0.05)
    style.SetPadLeftMargin (0.17)
    # style.SetPadRightMargin (0.03566265)
    style.SetPadRightMargin (0.065)
    style.SetPadGridX (0)
    style.SetPadGridY (0)
    style.SetPadTickX (1)
    style.SetPadTickY (1)
    # Frames
    style.SetLineWidth(3)
    style.SetFrameFillStyle ( 0)
    style.SetFrameFillColor ( 0)
    style.SetFrameLineColor ( 1)
    style.SetFrameLineStyle ( 0)
    style.SetFrameLineWidth ( 2)
    style.SetFrameBorderSize(10)
    style.SetFrameBorderMode( 0)
    # Histograms
    style.SetHistFillColor(2)
    style.SetHistFillStyle(0)
    style.SetHistLineColor(1)
    style.SetHistLineStyle(0)
    style.SetHistLineWidth(3)
    style.SetNdivisions(505)
    # Functions
    style.SetFuncColor(1)
    style.SetFuncStyle(0)
    style.SetFuncWidth(2)
    # Various
    style.SetMarkerStyle(20)
    style.SetMarkerColor(kBlack)
    style.SetMarkerSize (1.4)
    style.SetTitleBorderSize(0)
    style.SetTitleFillColor (0)
    style.SetTitleX (0.2)
    style.SetTitleSize (0.055,"X")
    style.SetTitleOffset(1.100,"X")
    style.SetLabelOffset(0.005,"X")
    style.SetLabelSize (0.050,"X")
    style.SetLabelFont (42 ,"X")
    style.SetStripDecimals(False)
    style.SetLineStyleString(11,"20 10")
    style.SetTitleSize (0.055,"Y")
    style.SetTitleOffset(1.5,"Y")
    style.SetLabelOffset(0.010,"Y")
    style.SetLabelSize (0.050,"Y")
    style.SetLabelFont (42 ,"Y")
    style.SetTextSize (0.055)
    style.SetTextFont (42)
    style.SetStatFont (42)
    style.SetTitleFont (42)
    style.SetTitleFont (42,"X")
    style.SetTitleFont (42,"Y")
    style.SetOptStat (0)

    style.SetLegendBorderSize(0)
    style.cd()

def cmsPrel(lumi,  energy,  simOnly,  onLeft=True,  sp=0, textScale=1.):
    latex = TLatex()
  
    t = gStyle.GetPadTopMargin()/(1-sp)
    tmpTextSize=0.75*t
    latex.SetTextSize(tmpTextSize)
    latex.SetNDC()
    textSize=latex.GetTextSize()
    textSize*=textScale

    latex.SetName("lumiText")
    latex.SetTextFont(42)

    lumyloc = 0.965
    cmsyloc = 0.893
    simyloc = 0.858
    if sp!=0:
        lumyloc = 0.945
        cmsyloc = 0.85
        simyloc = 0.8
    cmsalign = 31
    cmsxloc = 0.924
    if onLeft:
        cmsalign = 11
        cmsxloc = 0.204
    if (lumi > 0.):
        latex.SetTextAlign(31) # align left, right=31
        latex.SetTextSize(textSize*0.6/0.75)
        if(lumi > 1000. ):
            latex.DrawLatex(0.93,lumyloc,
                            " {lumi} fb^{{-1}} ({energy} TeV)".format(
                                lumi=lumi/1000.,
                                energy=energy
                            ))
        else:
            latex.DrawLatex(0.93,lumyloc,
                            " {lumi} pb^{{-1}} ({energy} TeV)".format(
                                lumi=lumi,
                                energy=energy
                            ))
  
    else:
        latex.SetTextAlign(31) # align right=31
        latex.SetTextSize(textSize*0.6/0.75)
        latex.DrawLatex(0.93,lumyloc," {energy} TeV".format(energy=energy))
  
 
    latex.SetTextAlign(cmsalign) # align left / right
    latex.SetTextFont(61)
    latex.SetTextSize(textSize)
    latex.DrawLatex(cmsxloc, cmsyloc,"CMS")
  
    latex.SetTextFont(52)
    latex.SetTextSize(textSize*0.76)
    
    if(simOnly):
        latex.DrawLatex(cmsxloc, simyloc,"Simulation")
    
        
class HistStyle:
    def __init__(self,
                 markerStyle = 8,
                 markerColor = 1,
                 markerSize = 1,
                 lineStyle = 1,
                 lineColor = None,
                 lineWidth = 2,
                 fillColor = None,
                 fillStyle = 0 ):
        self.markerStyle = markerStyle
        self.markerColor = markerColor
        self.markerSize = markerSize
        self.lineStyle = lineStyle
        if lineColor is None:
            self.lineColor = markerColor
        else:
            self.lineColor = lineColor
        self.lineWidth = lineWidth
        self.fillColor = fillColor
        self.fillStyle = fillStyle

    def format( self, hist):
        hist.SetMarkerStyle( self.markerStyle )
        hist.SetMarkerColor( self.markerColor )
        hist.SetMarkerSize( self.markerSize )
        hist.SetLineStyle( self.lineStyle )
        hist.SetLineColor( self.lineColor )
        hist.SetLineWidth( self.lineWidth )
        if self.fillColor is not None:
            hist.SetFillColor( self.fillColor )
        hist.SetFillStyle( self.fillStyle )

traditional_style = HistStyle(
    markerColor=4,
    markerStyle=21,
    lineColor=4,
    lineWidth=3,
    lineStyle=7
)
pf_style = HistStyle(
    markerColor=2,
    markerStyle=8,
    lineColor=2,
    lineWidth=3,
)


class CanvasRatio( TCanvas ):
    '''Produces a canvas with a ratio pad.
    
    The main pad is accessible through self.main
    The ratio pad through self.ratio
    '''
    def __init__(self, name, title, lumi, energy, simOnly):
        super(CanvasRatio, self).__init__(name, title)

        self.lumi = lumi
        self.energy = energy
        self.simOnly = simOnly

        bm_ = gStyle.GetPadBottomMargin()  
        tm_ = gStyle.GetPadTopMargin()
        lm_ = gStyle.GetPadLeftMargin()
        rm_ = gStyle.GetPadRightMargin()
  
        self.splitPad = 0.34
        self.cd()
        self.main = TPad("pMain","pMain",
                         0., self.splitPad ,1.,1.)
        
        self.ratio  = TPad("pRatio","pRatio",
                           0., 0. ,1.,self.splitPad)

        self.main.SetLeftMargin(lm_)
        self.main.SetRightMargin(rm_)
        self.main.SetTopMargin(tm_/(1-self.splitPad) )
        self.main.SetBottomMargin(0.02/(1-self.splitPad) )
        
        self.ratio.SetLeftMargin(lm_)
        self.ratio.SetRightMargin(rm_)
        self.ratio.SetTopMargin(0.01/self.splitPad)
        self.ratio.SetBottomMargin(bm_/self.splitPad)
        self.main.Draw()
        # cmsPrel(25000., 8., True, self.splitPad)
        self.ratio.Draw()

    def draw(self, hist, on_main, *args, **kwargs):
        yaxis = hist.GetYaxis()
        xaxis = hist.GetXaxis()
        if on_main:
            self.main.cd()
            yaxis.SetLabelSize( gStyle.GetLabelSize("Y")/(1-self.splitPad) )
            yaxis.SetTitleSize( gStyle.GetTitleSize("Y")/(1-self.splitPad) )
            yaxis.SetTitleOffset( gStyle.GetTitleOffset("Y")*(1-self.splitPad) )
            xaxis.SetLabelSize( 0 )
            xaxis.SetTitleSize( 0 )
            cmsPrel(self.lumi, self.energy, self.simOnly, True, self.splitPad)
            self.main.Update()
            
        else:
            self.ratio.cd()
            yaxis.SetLabelSize( gStyle.GetLabelSize("Y")/self.splitPad )
            yaxis.SetTitleSize( gStyle.GetTitleSize("Y")/self.splitPad )
            xaxis.SetLabelSize( gStyle.GetLabelSize("Y")/self.splitPad )
            xaxis.SetTitleSize( gStyle.GetTitleSize("Y")/self.splitPad )
            yaxis.SetTitleOffset( gStyle.GetTitleOffset("Y")*self.splitPad )
            yaxis.SetNdivisions(5,5,0)
            yaxis.SetRangeUser(0.71, 1.29)
        hist.Draw(*args, **kwargs)
        self.Update()
            
    def draw_legend(self, legend):
        self.legend = copy.deepcopy(legend)
        frac_main = 1 - self.splitPad
        y1 = self.legend.GetY1()
        y2 = self.legend.GetY2()
        self.legend.SetY2(1-(1-y2)/frac_main)
        self.legend.SetY1(1-(1-y1)/frac_main)
        self.legend.Draw()
        print '-'*50
        
if __name__ == "__main__":

    from ROOT import gStyle, TH1F, gPad, TLegend, TF1

    officialStyle(gStyle)
    # setTDRStyle()
    
    c1 = TCanvas("c1", "c1") 
    
    h = TH1F("h", "; p_{T} (GeV); stuff_{index}^{Power}", 50, -40000, 40000)
    h.Sumw2()
    gaus1 = TF1('gaus1', 'gaus')
    gaus1.SetParameters(1, 0, 5000)
    h.FillRandom("gaus1", 5000)
    h.Draw()
    pf_style.format(h)

    gPad.Update()

    h2 = TH1F("h2", "; p_{T} (GeV); stuff_{Index}^{Power}", 50, -40000, 40000)
    h2.Sumw2()
    gaus1.SetParameters(1, 0, 10000)
    h2.FillRandom("gaus1", 5000)
    h2.Draw("same")
    traditional_style.format(h2)

    legend_args = (0.645, 0.79, 0.985, 0.91, '', 'NDC')

    legend = TLegend(*legend_args)
    legend.SetFillStyle(0)
    legend.AddEntry(h, "PF", "p")
    legend.AddEntry(h2, "Traditional", "p")
    legend.Draw()
     
    cmsPrel(25000., 8., True)

    c2 = TCanvas("c2", "c2")
    h.Draw('hist')
    h2.Draw('histsame')
    legend2 = TLegend(*legend_args)
    legend2.SetFillStyle(0)
    legend2.AddEntry(h, "PF", "l")
    legend2.AddEntry(h2, "Traditional", "l")
    legend2.Draw()
    cmsPrel(-1, 8., True)    

    gPad.Update()

    cr  = CanvasRatio('cr', 'canvas with ratio', 25000, 8., True)
    h3 = h.Clone('h3')
    h4 = h2.Clone('h4')
    cr.draw(h3, True)
    cr.draw(h4, True, 'same')
    cr.draw_legend(legend)
    
    hratio = h3.Clone('hratio')
    hratio.Divide(h4)
    hratio.SetYTitle('ratio')
    cr.draw(hratio, False)
    gPad.Update()
    
    
    c1.SaveAs('c1.pdf')
    c2.SaveAs('c2.pdf')
    cr.SaveAs('cr.pdf')
