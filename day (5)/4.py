for i in range(20,23):
  print("obtained score and grade information of roll",i)
  for j in range(3):
    if j==0:
        number=int(input("obtained mark:bangla "))
        if number>=80:
            print("scored A+")
        else:
            print("scored below A+")
    elif j==1:
           number=int(input("obtainsed mark in english:"))
           if number>=80:
               print("scored A+")
           else:
               print("scored below A+")
    else:
          number=int(input("obtainsed mark in math:"))
          if number>=80:
               print("scored A+")
          else:
               print("scored below A+")