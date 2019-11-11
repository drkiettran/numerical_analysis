import sys

class Time_Value_Money():
    
    '''
    T1(i,n)
    '''
    def compounded_amount(self, i, n):
        return (1 + i)**n
    
    def T1(self, i, n):
        return self.compounded_amount(i, n)
    
    def T1_i(self, T1, n):
        return ((T1**(1.0/n)))-1
    
    ''' T2(i,n) '''
    def compounded_amount_of_annuity(self, i, n):
        return (((1 + i)**n)-1)/i
    
    def T2(self, i, n):
        return self.compounded_amount_of_annuity(i, n)
    
    def present_value_of(self, i, n):
        return 1 / ((1 + i)**n)
    
    def T3(self, i, n):
        return self.present_value_of(i, n)
    
    def present_value_of_an_annuity(self, i, n):
        return (1/i)*(1 - (1/((1+i)**n)))
    
    def T4(self, i, n):
        return self.present_value_of_an_annuity(i, n)
    
    def FV(self, P, i, n):
        return P*self.T1(i,n)
    
    def FV_intra_year(self, P, i, n, m):
        return P*self.T1(i/m, n*m)
    
    def FV_of_annuity(self, A, i, n, m):
        return A*self.T2(i/m, n*m)

    def PV(self, P, i, n):
        return P*self.T3(i,n)
    
    def PV_of_annuity(self, A, i, n):
        return A*self.T4(i, n)
    
    def deposit_to_accumulate_a_future_sum(self, S, i, n):
        return S/self.T2(i,n)
    
    def amortized_loan(self, P, i, n):
        return P/self.T4(i,n)
    
    def APR(self, i, m):
        return ((1 + (i/m))**m) - 1.0
    
    def rate_of_growth(self, FV, P, n):
        return self.T1_i(FV/P, n)
    
    '''
    I: interest pyament per period
    '''
    def bond_value(self, I, M, i, n):
        return I*self.T4(i,n) + M*self.T3(i,n)

    ''' Armotized payment '''
    def A(self, Pn, i, n):
        return Pn/self.T4(i,n)

    def Pn(self, A, i, n):
        return A*self.T4(i,n)        
    
    def sched(self, Pn, i, n):
        sched = []
        A = self.A(Pn, i, n)
        for j in range(0,n):
            sched.append(Pn)
            Pn = Pn*(1.0+i)
            Pn -= A
        sched.append(Pn)
        return A, sched
            
def formatFV(P, i, n, m):
    return 'P:{:,} i:{:.2f} n:{} m:{} FV:{:,.2f}'

def formatPV(P, i, n, m):
    return 'P:{:,} i:{:.2f} n:{} m:{} PV:{:,.2f}'

def main(argv):
    tvm = Time_Value_Money()
    print('T1 {}: {:.3f}'.format(1, tvm.T1(0.04, 40)))
    print('T2 {}: {:.3f}'.format(1, tvm.T2(0.04, 40)))
    print('T3 {}: {:.3f}'.format(1, tvm.T3(0.04, 40)))
    print('T4 {}: {:.3f}'.format(1, tvm.T4(0.04, 40)))
    P = 1000; i = 0.08; n = 4; m = 1
    print(formatFV(P, i, n, m).format(P, i, n, m, tvm.FV(P, i, n)))
    
    P = 10000; i = 0.2; n = 5; m = 4
    print(formatFV(P, i, n, m).format(P, i, n, m, tvm.FV_intra_year(P, i, n, m)))
    
    P = 1000; i = 0.08; n = 2; m = 1
    print(formatFV(P, i, n, m).format(P, i, n, m, tvm.FV_intra_year(P, i, n, m)))
    
    P = 1000; i = 0.08; n = 2; m = 2
    print(formatFV(P, i, n, m).format(P, i, n, m, tvm.FV_intra_year(P, i, n, m)))

    P = 1000; i = 0.08; n = 2; m = 4
    print(formatFV(P, i, n, m).format(P, i, n, m, tvm.FV_intra_year(P, i, n, m)))

    P = 1000; i = 0.08; n = 6; m = 1
    print(formatFV(P, i, n, m).format(P, i, n, m, tvm.FV_of_annuity(P, i, n, 1)))
    
    P = 30000; i = 0.08; n = 10; m = 2
    print(formatFV(P, i, n, m).format(P, i, n, m, tvm.FV_of_annuity(P, i, n, m)))

    P = 20000; i = 0.1; n = 6; m = 2
    print(formatPV(P, i, n, m).format(P, i, n, m, tvm.PV(P, i, n)))

    P = 10000; i = 0.1; n = 3; m = 1
    print(formatPV(P, i, n, m).format(P, i, n, m, tvm.PV_of_annuity(P, i, n)))

    P = 5000; i = 0.1; n = 5; m = 1
    print(formatPV(P, i, n, m).format(P, i, n, m, tvm.deposit_to_accumulate_a_future_sum(P, i, n)))

    P = 1000000; i = 0.1; n = 30; m = 1
    print(formatPV(P, i, n, m).format(P, i, n, m, tvm.deposit_to_accumulate_a_future_sum(P, i, n)))

    P = 200000; i = 0.14; n = 5; m = 1
    print(formatPV(P, i, n, m).format(P, i, n, m, tvm.amortized_loan(P, i, n)))

    P = 5000; i = 0.12; n = 40; m = 1
    print(formatPV(P, i, n, m).format(P, i, n, m, tvm.amortized_loan(P, i/12, n)))

    P = 2000; i = 0.12; n = 3; m = 1
    print(formatPV(P, i, n, m).format(P, i, n, m, tvm.amortized_loan(P, i, n)))
    
    i = .06; m = 4
    print('i:{:.2f} m:{} APR:{:.4f}'.format(i, m, tvm.APR(i, m)))

    FV = 3.7; P = 2.5; i = 0; n = 10; m = 1
    print('FV:{:.2f} P:{:.2f} i:{:.4f}'.format(FV, P, tvm.rate_of_growth(FV, P, n)))
    
    I = 50; M=1000; i=.06; n=20
    print('I:{:,} M:{:,} i:{:.2f} n:{} bond-value:{:,.2f}'.format(I, M, i, n, tvm.bond_value(I, M, i, n)))
    
    P5=200000.0; i=.14; n=5
    print('P5:${:,.2f} i:{:.0f}% n:{} A=${:,.2f}'.format(P5, 100*i, n, tvm.A(P5, i, n)))

    P40=5000.0; i=.12/12; n=40
    print('P40:${:,.2f} i:{:.0f}% n:{} A=${:,.2f}'.format(P40, 100*i, n, tvm.A(P40, i, n)))

    P3=2000.0; i=.12; n=3
    print('P3:${:,.2f} i:{:.0f}% n:{} A=${:,.2f}'.format(P3, 100*i, n, tvm.A(P3, i, n)))

    P40=5000.0; i=.12/12.0; n=40
    print('P40:${:,.2f} i:{:.0f}% n:{} A=${:,.2f}'.format(P40, 100*i, n, tvm.A(P40, i, n)))
  

    P120=600000.0; i=.03/12.0; n=120
    print('P40:${:,.2f} i:{:.0f}% n:{} A=${:,.2f}'.format(P120, 100*i*12, n, tvm.A(P120, i, n)))
    
    A, principles = tvm.sched(P120, i, n)
    count = 1
    for principle in principles:
        print('{:2}. payment: {:,.2f} principle: {:,.2f}'.format(count, A, principle))
        count += 1
    print('P40:${:,.2f} i:{:.0f}% n:{} A=${:,.2f}'.format(P120, 100*i*12, n, A))
    
if __name__ == '__main__':
    main(sys.argv[1:])
        