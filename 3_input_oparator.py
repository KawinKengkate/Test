#function input = รับค่าจากคีบอร์ด
'''name = input("Name : ")
surname = input("Surname :")
print("Your name is",name , surname)
print(type(name))'''

x = int(input("x : "))
y = input("y : ")
z = x + int(y)
print(z)
print(x + int(y))

#ตัวดำเนินการ & ตัวที่ถูกดำเนินการ
# x + y
# x, y => Operand
# + => Operator
x = 5
y = 10
print("บวก =", x+y)
print("ลบ  =", x-y)
print("คูณ  =", x*y)
print("หาร  =", x/y)
print("หารปัดเศษ =", x//y)
print("ยกกำลัง   =", x**y)
print("หารเอาเศษ =", x%y)