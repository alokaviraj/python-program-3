n=int(input("enter the cost of pen="))
pc=n*100             #pencost
if(pc>=1000):
    dis=(0.2*pc)
    tamount=(pc-dis)
    print(tamount)
else:
    dis=(0.1*pc)
    tamount=(pc-dis)
    print(tamount)
