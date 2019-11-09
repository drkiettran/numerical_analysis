import sys
import tvm

class Stock_And_Bond():
    def __init__(self):
        self.mytvm = tvm.TimeValueMoney()
    def security_value(self, CFs, r):
        sum = 0.0
        for t in range(0, len(CFs)):
            sum += ((CFs[t])/((1+r)**t))
        return sum
    '''
    I: intereswt payment each year - coupon interest rate x par value
    M: par value, or mature value, typical $1,000
    r = investor's required ROR
    n = number of year to maturity
    '''
    def BV(self, I, M, r, n):
        return I*self.mytvm.T4(r,n) + M*self.mytvm.T3(r,n)
        
    def BV_m(self, I, M, r, n, m):
        return I*self.mytvm.T4(r/m,n*m) + M*self.mytvm.T3(r/m,n*m)
        
    def Yield(self, I, M, V, n):
        return (I+((M-V)/n))/((M+V)/2.0)
    
    def PSV(self, D, r):
        return D/r
    
    def expected_ROR_PS(self, D, V):
        return D/V
    
    def CSV(self, divident, price, r):
        return divident*self.mytvm.T3(r,1) + price*self.mytvm.T3(r,1)
    
    def CSV_model(self, dividents, r):
        sum = 0.0
        for t in range(0, len(dividents)):
            sum += dividents[t]/((1+r)**(t+1))
        return sum
    
    def div_yield(self, D1, P0):
        return D1/P0
    
    def cap_gain_yield(self, CG, P0):
        return CG/P0
    
    def expected_ROR_CS(self, D1, CG, P0):
        return self.div_yield(D1, P0) + self.cap_gain_yield(CG, P0)
    
    def expected_ROR_CS_constant_D1(self, D1, g, P0):
        return self.div_yield(D1, P0) + g
    
def main(argv):
    snb = Stock_And_Bond()

    I=80; M=1000; r=.1; n=10
    print('I:{} M:{} r:{} n:{} BV: {:.2f}'.format(I, M, r, n, snb.BV(I, M, r, n)))

    I=40; M=1000; r=.1; n=10; m = 2
    print('I:{} M:{} r:{} n:{} BV: {:.2f}'.format(I, M, r, n, snb.BV_m(I, M, r, n, m)))
    
    I=80; M=1000; V=877.6; n = 10
    print('I:{} M:{} V:{:.2f} n:{} Yield: {:.2f}%'.format(I, M, V, n, snb.Yield(I, M, V, n)*100))
    
    D=4; r=.16
    print('D:${:.2f} r:{:.0f}% V:${:.2f}'.format(D, r*100, snb.PSV(D,r)))

    D=5.0; V=25.0
    print('D:${:.2f} V:${:.2f} r:{:.0f}%'.format(D, V, snb.expected_ROR_PS(D,V)*100))
    
    D1=1.5; P1=40.0; r=.15
    print('D1:${:.2f} P1:${:.2f} r:{:.2f}% CSV:${:.2f}'.format(D1, P1, r, snb.CSV(D1, P1, r)))
    
    D=2.5; r=.1
    print('D:{} r:{:.2f}% P:${:.2f}'.format(D, 100*r, D/r))
    
    D=3; r=.12; g=.1
    print('D:{} r:{:.2f}% g:{:.2f}% P:${:.2f}'.format(D, 100*r, 100*g, (D*(1+g))/(r-g)))
    
    P0=50.0; P1=55.0; D1=3.0
    print('D:${:.2f} P0:${:.2f} P1:${:.2f} ROR:{:.0f}%'.format(D1, P0, P1, snb.expected_ROR_CS(D1, P1-P0, P0)*100))
    
    P0=30.0; D1=4.5; g=.06
    print('D:${:.2f} P0:${:.2f} g:${:.2f} ROR:{:.0f}%'.format(D1, P0, g, snb.expected_ROR_CS_constant_D1(D1, g, P0)*100))
    
if __name__ == '__main__':
    main(sys.argv[1:])    