
class que:
    def __init__(self,n):
        self.size=n
        self.q=[0 for i in range(n)]
        self.f=-1
        self.r=-1
    def enque(self,x):
        if(self.f==-1):
            self.f=0
            self.r=0
            self.q[self.r]=x
        elif(self.r==self.size-1):
            print("queue is full")
        else:
            self.r+=1 
            self.q[self.r]=x 
    def deque(self):
        if(self.f==1):
            print("no element to deque")
        elif(self.f==self.r):
            self.f=-1 
            self.r=-1 
        else:
            print("dequeued element is",self.q[self.f])
            for i in range(1,self.r+1):
                self.q[i-1]=self.q[i]
            self.r-=1 
    def display(self):
        if(self.f==-1):
            print("no element to display")
        else:
            print("queue elements are:")
            for i in range(self.f,self.r+1):
                print(self.q[i],end="")
                
                
size=int(input("\nenter size"))
s=que(size)
while(True):
    
    
    print("\n1.enque\n2.deque\n3.display\n4.exit")
    ch=int(input("\nenter ur choice"))
    if(ch==1):
        x=int(input("enter elements"))
        
        s.enque(x)
    elif(ch==2):
        s.deque()
    elif(ch==3):
        s.display()
    elif(ch==4):
        break
    else:
        print("invalid choice")
        
    