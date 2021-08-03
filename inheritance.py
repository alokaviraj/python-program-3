class teacher:
        def display(self,show):
             print("hello i m inheritance");
             self.show();
        tid=0
        tname="null"
        def show(self):
           self.tid=int(input("enter the id:-"))
           self.tname=(input("enter the name:-"))
           print("tid=",self.tid)
           print("tname=",self.tname)
class test(teacher):
        def display(self):       
          print("hello i m inheritance")
t1=test();
t1.display();
t1.show();

