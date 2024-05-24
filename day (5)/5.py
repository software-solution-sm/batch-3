while True:
  number1=input("enter the number1:")
  number1=int(number1)
  number2=input("enter the number2:")
  number2=int(number2)
  if number2==0:
    break
  else:
    result=number1/number2
    print("result:",result)
    continue