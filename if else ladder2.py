a=int(input("enter the marks"))
b=int(input("enter the marks"))
c=int(input("enter the marks"))
tmarks=(a+b+c)
print(tmarks)
tp=(tmarks/3)
print(tp)
if(tp>=75):
     print("gradeA")
elif(tp>=60):
    print("gradeB")
elif(tp>=40):
    print("gradeC")
else:
    print("pass")
