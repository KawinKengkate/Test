#data type
a = 1 #ตัวแปร a เก็บข้อมูล Integer
b = 1.5 #ตัวแปร b เก็บข้อมูล Floating
d = "Kawin Kengkate" #ตัวแปร d เก็บข้อมูล String
e = True #ตัวแปร e เก็บข้อมูล Boolean
print(d + " got grade ",a+b )

print(type(a)) #คำสั่งtype แสดงชนิดข้อมูล
print(type('H'))
print(type(e))
print()

_a = 15

#Type Convertion
x = 10
y = 3.14
z = "20"
result1 = x+y # 10 + 3.14 = 13.14
print(type(x))
print(type(y))
print(type(z))

print("result1 type " ,type(result1))
print("result1 = ",result1)

#string => integer
result2 = x+int(z)
print("result2 = " ,result2)

#integer => string
result3 = str(x) + z
print("result3 = ",result3)

#string => floating
print("float z = ",float(z))

#floating => integer
print("integer y = ",int(y))