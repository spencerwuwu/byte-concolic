def reverseCheck(number):
  originalNum = number
  reverseNum=0
  while(number > 0):
    reminder = number % 10
    reverseNum  = (reverseNum *10) + reminder
    number = number // 10
  if(originalNum  == reverseNum):
    return True
  else:
    return False
    
print(reverseCheck(121))
