#instance methods
#class methods
#static methods

class Test:
    x=5 # class variable / static variable
    
    def __init__(self,a,b):
        self.a=a
        self.b=b
        
    #instance method
    def show(self):
        print(f'a is:{self.a} and b is:{self.b}')
        
    #class methods
    @classmethod
    def f2(cls): #cls represtent class
        print(f'x is :{cls.x}')
        
    #static methods
    @staticmethod
    def stat(): # youw wish to give parameter or not
        print("hello")
        
t1 = Test(3,4)
t2 = Test(4,6)
t1.show() # calling instance method

#calling for static method
t1.stat() #call for instance object
Test.stat() #call for class object

#calling for class static method
Test.f2()
t1.f2()