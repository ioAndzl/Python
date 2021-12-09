import inspect 

class Origin():
    """."""
    def __init__(self,a ,b ,c):
        self.a = a
        self.b = b
        self.c = c
    
    def mOrigin1():
        print(f'first origin method')

    def mOrigin2():
        print(f'secound origin method')

class Root(Origin):
    """."""
    def __init__(self,d ,e ,f):
        super().__init__(d, e, f)
        self.d = d
        self.e = e
        self.f = f
    
    def mRoot1():
        print(f'first origin method')

    def mRoot2():
        print(f'secound origin method')

if __name__=='__main__':
    oo = Origin(1,2,3)
    rr = Root(4,5,6)
    # print(vars(rr))
