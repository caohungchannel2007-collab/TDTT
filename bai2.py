import math
a = float(input("chieu dai :"))
b = float(input("cheu rong :"))
s = a*b
r = b/2
d = s - (r**2)*math.pi
#có thể dùng u = round(d, 2) để làm tròn 
print(f"dien tich phan trong cay la :{d:.2f}")