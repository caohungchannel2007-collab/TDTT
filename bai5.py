chu_hoa = input("nhap vao chu cai in hoa:")
if chu_hoa == 'A':
 print ("khong co ket qua")
elif ( 'a' <= chu_hoa <= 'z' ) :
 print("may bi mu a, stupid")
else :
 chu_thuong = chu_hoa.lower()
 ordinal = ord(chu_thuong)-1
 character = chr(ordinal) 
 print(f"ket qua la: {character}{chu_hoa}")

  

