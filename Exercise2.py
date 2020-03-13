error_msg_numeric = "Error, please enter numeric input"

hours = raw_input('Enter Hours:')
try:
  float(hours)>=0
except:
  print (error_msg_numeric)
  hours = raw_input('Enter Hours:')

rate = raw_input('Enter Rate:')
try:
  float(rate) >=0
except:
  print (error_msg_numeric)
  rate = raw_input('Enter Rate:')

hours = float(hours)
rate = float(rate)

if hours > 40:
  extra_time = hours - 40
else:
  extra_time = 0

extra_pay = 0.5 * rate * extra_time

pay = hours * rate + extra_pay

print ('Pay: '),
print pay
