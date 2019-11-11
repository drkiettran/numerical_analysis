#!/usr/bin/python3

import sys
import tvm

def print_sched(original_principle, rate, years):
    my_tvm = tvm.Time_Value_Money()
    A, principles = my_tvm.sched(original_principle, rate/12.0, years*12)
    total_payment = A*years*12
    count = 1
    for principle in principles:
        print('{:2}. payment: {:,.2f} principle: {:,.2f}'.format(count, A, principle))
        count += 1
    print('principle: {:,.2f} rate: {:,.5f} years: {:.0f}'.format(principle, rate, years))
    print('monthly: {:,.2f} total payment: {:,.2f}  total interest {:,.2f}'.\
            format(A, total_payment, total_payment-original_principle))
    
def main(argv):
    princ = argv[0]
    rate = argv[1]
    years = argv[2]
    print_sched(float(princ), float(rate), int(years))

if __name__ == '__main__':
    main(sys.argv[1:])