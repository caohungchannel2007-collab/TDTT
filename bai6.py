import math

a,b,c = map(float,input().split())
if a+b>c and a+c>b and b+c>a  and a>0 and b>0 and c>0 :
    p = (a+b+c)/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(f"dien tich cua tam giac = {s:.2f}")
else :
    print("khong phai 3 canh cua tam giac")