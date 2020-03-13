error_msg_invalid = "ERROR: Invalid input."
input_score = raw_input('Enter a score between 0.0 and 1.0: ')
try:
  if (float(input_score) >= 0) and ( float(input_score) <= 1 ):
    print('valid input, thanks!')
  else:
    print (error_msg_invalid)
    input_score = raw_input('Enter a score between 0.0 and 1.0: ')
except:
  print (error_msg_invalid)
  input_score = raw_input('Enter a score between 0.0 and 1.0: ')

input_score = float(input_score)

if input_score < 0.6:
  print ('F')

elif input_score >= 0.9:
  print ('A')

elif input_score >= 0.8:
  print ('B')

elif input_score >= 0.7:
  print('C')

elif input_score >= 0.6:
  print('D')

else:
  print ('Invalid')
