#!/usr/bin/python3
import sys
import tvm



def main(argv):
    time_value_money = tvm.Time_Value_Money()
    loan_amount = float(argv[0])
    yearly_rate = float(argv[1])
    num_years = int(argv[2])
    monthly,months = time_value_money.sched(loan_amount, yearly_rate/12.0, num_years * 12)
    for month in months:
        print('{:,.2f}, {:,.2f}'.format(monthly, month))
    
if __name__ == '__main__':
    main(sys.argv[1:])