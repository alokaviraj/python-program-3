class teacher:
    tid=0
    tname="null"
    def show(self):
        self.tid=int(input("enter the id"))
        self.tname=(input("enter the name"))
        print("tid=",self.tid)
        print("tname=",self.tname)
            
t1=teacher();
t1.show();
