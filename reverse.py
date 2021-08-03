n=int(input("enter the number"))
R=0
rem=n%10
R=R*10+rem
n=int(n/10)
rem=n%10
R=R*10+rem
n=int(n/10)
R=R*10+n
print(R)
      
      
      
