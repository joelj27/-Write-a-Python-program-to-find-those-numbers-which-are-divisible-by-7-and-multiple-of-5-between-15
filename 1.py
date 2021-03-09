print("enter the number")
a=int(input("enter the stating number:"))
b=int(input("enter the ending number:"))
while a<1500:
      print("enter the number greater than 1500")
      break
while b<2700:
       print("enter the number less than 2700")
       break
for i in range(a,b):
    if (i%7==0) and (i%5==0):
        print(i)