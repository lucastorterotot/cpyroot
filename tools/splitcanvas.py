from ROOT import TCanvas

import math

def divisors(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

def div_1_2(n):
    divs = list(divisors(n))
    if len(divs) == 2:
        n += 1  # prime number, going for next even number
    print n
    pdist = n
    pd1 = None
    pd2 = None
    for d1 in divisors(n):
        d2 = n / d1
        dist = abs(d2-d1)
        print d2, d1, dist, pdist
        if dist >= pdist:
            if pd1 is None:
                pd1, pd2 = d1, d2
            return pd1, pd2
        else:
            pdist, pd1, pd2 = dist, d1, d2
            
class SplitCanvas(TCanvas):
    '''TCanvas with automatic splitting according to the number of plots to be done'''
    
    def __init__(self, nplots, name, title, padsize):
        '''Provide the number of plots and the TCanvas arguments'''
        d1, d2 = div_1_2(nplots)
        cx = d2 * padsize
        cy = d1 * padsize
        super(SplitCanvas, self).__init__(name, title, cx, cy)
        self.Divide(d2, d1)
        self.Draw()
        
        
