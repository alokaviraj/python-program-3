n=int(input("enter the three digit number"))
sum=0
rem=n%10
sum=sum+rem
n=int(n/10)
rem=n%10
sum=sum+rem
n=int(n/10)
rem=n%10
sum=sum+rem
print(sum)

