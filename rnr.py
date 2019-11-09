import sys
import math


class ReturnAndRisk():
    def HPR(self, CI, CG, PP):
        return (CI+CG)/PP
    
    def AR(self, rates, n):
        sum = 0.0
        for rate in rates:
            sum += rate
        return sum/n
    
    def GR(self, rates, n):
        prod = 1.0
        for rate in rates:
            prod *= (1.0+rate)
        return prod**(1.0/n) - 1.0
    
    def expected_ROR(self, rates, probs):
        r = 0.0
        for i in range(0, len(rates)):
            r += (rates[i]*probs[i])
        return r
    
    def risk(self, rates, probs):
        r = self.expected_ROR(rates, probs)
        sum = 0.0
        for i in range(0, len(rates)):
            sum += ((rates[i] - r)**2)*probs[i]
        return math.sqrt(sum)
    
    def coeff(self, rates, probs):
        return self.risk(rates, probs)/self.expected_ROR(rates, probs)
    
    def risk_premium(self, rf, rm, beta):
        return rf+(beta*(rm-rf))
    
def main(argv):
    rnr = ReturnAndRisk()
    
    PP = 100; CG = 13; SP=107; CI=SP-PP
    print('CI:{:,.2f} CG:{:,.2f} PP:{:,.2f} HPR:{:.0f}%'.format(CI, CG, PP, rnr.HPR(CI, CG, PP)*100))

    PP = 100; CG = 18; SP=97; CI=SP-PP
    print('CI:{:,.2f} CG:{:,.2f} PP:{:,.2f} HPR:{:.0f}%'.format(CI, CG, PP, rnr.HPR(CI, CG, PP)*100))
    
    rates=[1.0, -.5]; n = 2
    print('AR:{:.0f}%'.format(rnr.AR(rates,n)*100))

    rates=[1.0, -.5]; n = 2
    print('GR:{:.0f}%'.format(rnr.GR(rates,n)*100))
    
    rates=[-.05, .2, .4]; probs=[.2, .6, .2]
    print('expected ROR:{:.0f}%'.format(rnr.expected_ROR(rates, probs)*100))
    print('risk:{:.2f}%'.format(rnr.risk(rates, probs)*100))
    print('coeff:{:.2f}'.format(rnr.coeff(rates, probs)))
    
    rates=[.1, .15, .2]; probs=[.2, .6, .2]
    print('expected ROR:{:.0f}%'.format(rnr.expected_ROR(rates, probs)*100))
    print('risk:{:.2f}%'.format(rnr.risk(rates, probs)*100))
    print('coeff:{:.2f}'.format(rnr.coeff(rates, probs)))
    
    print('risk_premium:{:.0f}%'.format(rnr.risk_premium(.06, .1, 2.0)*100))
    
if __name__ == '__main__':
    main(sys.argv[1:])