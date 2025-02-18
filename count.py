'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
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
    def level_t(self):
        q=[]
        q.append(self.root)
        c=0
        while(len(q)!=0):
            c+=1
            t=q.pop(0)
            
            if(t.left!=None):
                q.append(t.left)
            if(t.right!=None):
                q.append(t.right)
        return c
b=btree()
x=int(input("enter the root node"))
a=node(x)
b.root=a 
b.insert()

k=b.level_t()
print("no. of nodes= ",k)