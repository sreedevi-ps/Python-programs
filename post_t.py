class node:
    def __init__(self,x):
        self.data=x
        self.left=None
        self.right=None
class btree:
    def __init__(self):
        self.root=None
    def insert(self):
        q=[]
        q.append(self.root)
        while(len(q)!=0):
            t=q.pop(0)
            x1=int(input("enter left child"))
            if(x1!=-1):
                a1=node(x1)
                t.left=a1
                q.append(a1)
            x2=int(input("enter right child"))
            if(x2!=-1):
                a2=node(x2)
                t.right=a2
                q.append(a2)
    def post(self,p):
       if(p==None):
           return 0
       
       b.post(p.left)
       b.post(p.right)
       print(p.data)
b=btree()
x=int(input("enter the root node"))
a=node(x)
b.root=a 
b.insert()
'''b.level_t()'''
b.post(a)