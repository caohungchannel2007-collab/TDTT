import math 
a = float(input("gia tri cua a la :"))
b = float(input("gia tri cua b la :"))
c = float(input("gia tri cua c la :"))
if a!=0 :
 if b%2==0 :
  b1 = b/2
  denta_p = b1**2 - a*c
  if denta_p >= 0 :
   x1 = (-b1-math.sqrt(denta_p))/(a)
   x2 = (-b1+math.sqrt(denta_p))/(a)
   print(f"x1 = {x1} , x2 = {x2} ")
  else :
   print("phuong trinh vo nghiem")
 else :
  denta = b**2 - 4*a*c
  if denta >= 0 :
   x1 = (-b-math.sqrt(denta))/(2*a)
   x2 = (-b+math.sqrt(denta))/(2*a)
   print(f"x1 = {x1} , x2 = {x2}")
  else :
   print("phuong trinh vo nghiem ")
else:
 x = -c/b
 print(x)
 

