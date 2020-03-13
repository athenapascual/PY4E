hours = raw_input('Enter Hours: ')
rate = raw_input('Enter Rate: ')

if hours > 40:
  extra_time = float(hours) - 40
else:
  extra_time = 0

extra_pay = 0.5 * float(rate) * extra_time

pay = float(hours) * float(rate) + extra_pay

print ('Pay:475.0 '),
print pay
