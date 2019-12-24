#!/usr/bin/python3
import sys

"""
Time vale money functions
"""


class TimeValueMoney:

    @staticmethod
    def compounded_amount(i, n):
        return (1 + i) ** n

    def t1(self, i, n):
        return self.compounded_amount(i, n)

    @staticmethod
    def t1_i(t1, n):
        return (t1 ** (1.0 / n)) - 1

    ''' T2(i,n) '''

    @staticmethod
    def compounded_amount_of_annuity(i, n):
        return (((1 + i) ** n) - 1) / i

    def t2(self, i, n):
        return self.compounded_amount_of_annuity(i, n)

    @staticmethod
    def present_value_of(i, n):
        return 1 / ((1 + i) ** n)

    def t3(self, i, n):
        return self.present_value_of(i, n)

    @staticmethod
    def present_value_of_an_annuity(i, n):
        return (1 / i) * (1 - (1 / ((1 + i) ** n)))

    def t4(self, i, n):
        return self.present_value_of_an_annuity(i, n)

    def fv(self, p, i, n):
        return p * self.t1(i, n)

    def fv_intra_year(self, p, i, n, m):
        return p * self.t1(i / m, n * m)

    def fv_of_annuity(self, a, i, n, m):
        return a * self.t2(i / m, n * m)

    def pv(self, p, i, n):
        return p * self.t3(i, n)

    def pv_of_annuity(self, a, i, n):
        return a * self.t4(i, n)

    def deposit_to_accumulate_a_future_sum(self, s, i, n):
        return s / self.t2(i, n)

    def amortized_loan(self, p, i, n):
        return p / self.t4(i, n)

    @staticmethod
    def apr(i, m):
        return ((1 + (i / m)) ** m) - 1.0

    def rate_of_growth(self, fv, p, n):
        return self.t1_i(fv / p, n)

    '''
    I: interest pyament per period
    '''

    def bond_value(self, I, m, i, n):
        return I * self.t4(i, n) + m * self.t3(i, n)

    ''' Armotized payment '''

    def a(self, pn, i, n):
        return pn / self.t4(i, n)

    def pn(self, a, i, n):
        return a * self.t4(i, n)

    def sched(self, pn, i, n):
        sched = []
        a = self.a(pn, i, n)
        for j in range(0, n):
            sched.append(pn)
            pn = pn * (1.0 + i)
            pn -= a
        sched.append(pn)
        return a, sched


def format_fv(p, i, n, m):
    return 'P:{:,} i:{:.2f} n:{} m:{} FV:{:,.2f}'


def format_pv(p, i, n, m):
    return 'P:{:,} i:{:.2f} n:{} m:{} PV:{:,.2f}'


def main(argv):
    tvm = TimeValueMoney()
    print('T1 {}: {:.3f}'.format(1, tvm.t1(0.04, 40)))
    print('T2 {}: {:.3f}'.format(1, tvm.t2(0.04, 40)))
    print('T3 {}: {:.3f}'.format(1, tvm.t3(0.04, 40)))
    print('T4 {}: {:.3f}'.format(1, tvm.t4(0.04, 40)))
    p = 1000
    i = 0.08
    n = 4
    m = 1
    print(format_fv(p, i, n, m).format(p, i, n, m, tvm.fv(p, i, n)))

    p = 10000
    i = 0.2
    n = 5
    m = 4
    print(format_fv(p, i, n, m).format(p, i, n, m, tvm.fv_intra_year(p, i, n, m)))

    p = 1000
    i = 0.08
    n = 2
    m = 1
    print(format_fv(p, i, n, m).format(p, i, n, m, tvm.fv_intra_year(p, i, n, m)))

    p = 1000
    i = 0.08
    n = 2
    m = 2
    print(format_fv(p, i, n, m).format(p, i, n, m, tvm.fv_intra_year(p, i, n, m)))

    p = 1000
    i = 0.08
    n = 2
    m = 4
    print(format_fv(p, i, n, m).format(p, i, n, m, tvm.fv_intra_year(p, i, n, m)))

    p = 1000
    i = 0.08
    n = 6
    m = 1
    print(format_fv(p, i, n, m).format(p, i, n, m, tvm.fv_of_annuity(p, i, n, 1)))

    p = 30000
    i = 0.08
    n = 10
    m = 2
    print(format_fv(p, i, n, m).format(p, i, n, m, tvm.fv_of_annuity(p, i, n, m)))

    p = 20000
    i = 0.1
    n = 6
    m = 2
    print(format_pv(p, i, n, m).format(p, i, n, m, tvm.pv(p, i, n)))

    p = 10000
    i = 0.1
    n = 3
    m = 1
    print(format_pv(p, i, n, m).format(p, i, n, m, tvm.pv_of_annuity(p, i, n)))

    p = 5000
    i = 0.1
    n = 5
    m = 1
    print(format_pv(p, i, n, m).format(p, i, n, m, tvm.deposit_to_accumulate_a_future_sum(p, i, n)))

    p = 1000000
    i = 0.1
    n = 30
    m = 1
    print(format_pv(p, i, n, m).format(p, i, n, m, tvm.deposit_to_accumulate_a_future_sum(p, i, n)))

    p = 200000
    i = 0.14
    n = 5
    m = 1
    print(format_pv(p, i, n, m).format(p, i, n, m, tvm.amortized_loan(p, i, n)))

    p = 5000
    i = 0.12
    n = 40
    m = 1
    print(format_pv(p, i, n, m).format(p, i, n, m, tvm.amortized_loan(p, i / 12, n)))

    p = 2000
    i = 0.12
    n = 3
    m = 1
    print(format_pv(p, i, n, m).format(p, i, n, m, tvm.amortized_loan(p, i, n)))

    i = .06
    m = 4
    print('i:{:.2f} m:{} APR:{:.4f}'.format(i, m, tvm.apr(i, m)))

    FV = 3.7
    p = 2.5
    i = 0
    n = 10
    m = 1
    print('FV:{:.2f} p:{:.2f} i:{:.4f}'.format(FV, p, tvm.rate_of_growth(FV, p, n)))

    I = 50
    M = 1000
    i = .06
    n = 20
    print('I:{:,} M:{:,} i:{:.2f} n:{} bond-value:{:,.2f}'.format(I, M, i, n, tvm.bond_value(I, M, i, n)))

    P5 = 200000.0
    i = .14
    n = 5
    print('P5:${:,.2f} i:{:.0f}% n:{} a=${:,.2f}'.format(P5, 100 * i, n, tvm.a(P5, i, n)))

    p_40 = 5000.0
    i = .12 / 12
    n = 40
    print('p_40:${:,.2f} i:{:.0f}% n:{} a=${:,.2f}'.format(p_40, 100 * i, n, tvm.a(p_40, i, n)))

    P3 = 2000.0
    i = .12
    n = 3
    print('P3:${:,.2f} i:{:.0f}% n:{} a=${:,.2f}'.format(P3, 100 * i, n, tvm.a(P3, i, n)))

    p_40 = 5000.0
    i = .12 / 12.0
    n = 40
    print('p_40:${:,.2f} i:{:.0f}% n:{} a=${:,.2f}'.format(p_40, 100 * i, n, tvm.a(p_40, i, n)))

    p_120 = 650000.0
    i = .03 / 12.0
    n = 120
    print('p_40:${:,.2f} i:{:.0f}% n:{} a=${:,.2f}'.format(p_120, 100 * i * 12, n, tvm.a(p_120, i, n)))

    a, principles = tvm.sched(p_120, i, n)
    count = 1
    for principle in principles:
        print('{:2}. payment: {:,.2f} principle: {:,.2f}'.format(count, a, principle))
        count += 1
    print('p_40:${:,.2f} i:{:.0f}% n:{} a=${:,.2f}'.format(p_120, 100 * i * 12, n, a))

    p_180 = 650000.0
    i = .03 / 12.0
    n = 180
    print('p_40:${:,.2f} i:{:.3f}% n:{} a=${:,.2f}'.format(p_180, 100 * i * 12, n, tvm.a(p_180, i, n)))

    a, principles = tvm.sched(p_180, i, n)

    count = 1
    for principle in principles:
        print('{:2}. payment: {:,.2f} principle: {:,.2f}'.format(count, a, principle))
        count += 1
    print('p_180:${:,.2f} i:{:.3f}% n:{} a=${:,.2f}'.format(p_180, 100 * i * 12, n, a))
    print('total:', a * n)


if __name__ == '__main__':
    main(sys.argv[1:])
