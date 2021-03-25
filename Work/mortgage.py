# mortgage.py
#
# Exercise 1.7

# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
i = 1
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000


while principal > 0:
    if (i >= extra_payment_start_month) & (i <= extra_payment_end_month):
        payment = 2684.11 + extra_payment
    else:
        payment = 2684.11
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment
    print(i , round(total_paid,2), round(principal,2))
    i += 1

print('Total Paid' , round(total_paid,2))
print('Months', i-1)