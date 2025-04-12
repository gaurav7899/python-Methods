#1
class Person:
    
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def show(self):
        print("My name is:",self.name)
        print("My age is:",self.age)
        
p=Person("gaurav",25)
p.show()

#2
import math
class Circle:
    p=math.pi
    def __init__(self,radius):
        self.__radius = radius
        
    def getter(self):
        return self.__radius
    
    def setter(self,value):
        self.__radius = value
        return self.__radius
    
    def getarea(self):
        return (Circle.p * self.__radius ** 2)
    
    def getCircumference(self):
        return (2* Circle.p *self.__radius)
    
c=Circle(2)
print(c.getter())
print(c.setter(5))
print(c.getarea())
print(c.getCircumference())

#3
class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    
    def setDeminsion(self,l,b):
        self.length = l
        self.breadth = b
        print("your rectangle length is:",self.length)
        print("your rectangle breadth is:",self.breadth)
        
    def showDimension(self):
        print("recangle dimension is:",self.length,self.breadth)
        
    def getArea(self):
        return (self.length* self.breadth)
    
rect = Rectangle(3,4)
setdim = rect.setDeminsion(5,7)
print(setdim)
print(rect.getArea())

#5
class Team:
    
    def __init__(self):
        self.name_list = []
        self.input_member_name()
        
    def input_member_name(self):
        input_user = input("""press given number
                        1.enter the team member
                        2.exit""")
        if input_user == "1":
            self.set_name()
        elif input_user =="2":
            exit()
        else:
            print("invalid input")
    
    def set_name(self):
        while True:
            name = input("enter the name:")
            if name=='0':
                break
            elif name ==str(name):
                self.name_list.append(name)
            else:
                print("invalid name")
                
    def show_name_list(self):
        return self.name_list
            
t=Team()
print(t.show_name_list())

#4
class Book:
    
    def __init__(self,bookID,title,price):
        self.bookid = bookID
        self.title = title
        self.price = price
        
    def show_book_variables(self):
        print(f"bookId: {self.bookid} \n title:{self.title} \n price:{self.price} ")
        
b=Book(101,"python",499)
b.show_book_variables()
