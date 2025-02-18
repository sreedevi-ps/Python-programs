

class node:
    def __init__(self,x):
        self.data=x 
        self.left=None 
        self.right=None 
class bstree:
    def __init__(self):
        self.root=None 
    def insert(self,x):
        a=node(x)
        if(self.root==None):
            self.root=a 
        else:
            p1=self.root
            p2=self.root
            while(p1!=None):
                p2=p1
                if(p1.data<a.data):
                    p1=p1.right
                    
                else:
                    p1=p1.left
            if(p2.data<a.data):
                    p2.right=a
            else:
                    p2.left=a 
                    
    def inorder(self,p):
            if(p==None):
                return 0 
            self.inorder(p.left)
            print(p.data)
            self.inorder(p.right)
    def height(self,p):
         if(self.p==None):
              return 0
         ld=self.height(p.left)
         rd=self.height(p.right)
         if(ld<rd):
              return rd+1
         else:
              return ld+1
              
bs=bstree()

bs.insert(10)
bs.insert(5)
bs.insert(15)
bs.insert(20)
bs.insert(18)
bs.insert(8)
bs.insert(9)
k=bs.height(bs.root)
print("height=",k)
'''bs.inorder(bs.root)'''

