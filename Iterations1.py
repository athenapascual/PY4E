count = 0
total = 0
avg = 0
keepgoing = True
while keepgoing:
  prompt1 = 'Enter a number \n'
  line = input (prompt1)
  try:
     line = float(line)
     count = count + 1 
     total = total + line
     avg = total / count
  except:
    if line == 'Done' or line == 'done':
      break
    else:
      print 'Invalid Input'
      continue
print count, total, avg

