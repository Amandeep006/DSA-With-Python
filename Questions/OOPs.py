"""
Access Specifier in the OOPS :
There are three access specifier in the programming language and in python also same.
1. Public 2. Private and 3. Protected
"""
# class Student:
#     name="a"
#     age=0
#     # _password="" # It show that this attribute is protected.
#     __password="" # It show that this attribute is private. It gives error if we print this attribute.

#     @property
#     def password(self):
#         print("getter is called")
#         return self.__password
    
#     @password.setter
#     def password(self,newPass):
#         print("setter is called")
#         self.__password=newPass


# S1=Student()
# S1.password="123"
# print(S1.password)


"""
Write a Python program to create a class named Vehicle that has no variables or methods defined inside it.
"""

# class Vechicle :
#      pass

# print(Vechicle)

"""
Write a Python program to create a Vehicle class with two instance attributes: 
max_speed and mileage. Create an object of the class and print both attributes.
"""

# class Vechicle:
#     def __init__(self, name,max_speed,mileage):
#         self.name=name
#         self.max_speed=max_speed
#         self.mileage=mileage
   

# car1=Vechicle("Tesla",100,200)
# print(f"Vechicle name : {car1.name} with {car1.max_speed}km/hr Speed and {car1.mileage} Mileage.")


"""
Write a Python program to create a Rectangle class with length and width as instance attributes, and two methods: area() that returns the area and perimeter() that returns the perimeter.
"""
# class Rectangle:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
    
#     def area(self):
#         result=self.length*self.breadth
#         return result 
    
#     def parameter(self):
#         result=2*(self.length+self.breadth)
#         return result
    
# len=int(input("Enter the length :"))
# bre=int(input("Enter the breadth :"))

# Rea1=Rectangle(len,bre)

# print(f"Area of Rectangle: {Rea1.area()}\nPerimeter of Rectangle : {Rea1.parameter()}")


"""
Write a Python program to create a Student class that stores a student's name and a list of marks. Add a method average() that calculates and returns the average of all marks.
"""

# class Student:
#     Sum=0
#     def __init__(self, name, marks):
#         self.name=name
#         self.marks=marks

#     def average(self):
#         return sum(self.marks)/len(self.marks)



# s1 = Student("Alice", [85, 90, 78, 92, 88])
# print(f"{s1.name}'s Average Grade: {s1.average()}")

  
"""
Write a Python program to create a Product class with three instance attributes: name, price, and quantity. Add a method total_value() that returns the total stock value by multiplying price by quantity.
"""

# class Product:
#     def __init__(self,name,price,quantity):
#         self.name=name
#         self.price=price
#         self.quantity=quantity

#     def total_value(self):
#         return self.price*self.quantity
    

# p1=Product("Laptop", 899.99, 5)
# print(f"Total stock value of {p1.name} : ₹{p1.total_value()}")


"""
Write a Python program to create a BankAccount class with a balance attribute and two methods: deposit(amount) that adds funds to the balance, and withdraw(amount) that deducts funds but prevents the balance from going below zero.
"""

# class BankAccount:
#     def __init__(self, balance):
#         self.balance=balance
        
    
#     def deposit(self,fund):
#         self.balance+=fund
#         return self.balance

#     def withdrawl(self,fund):
#         if (self.balance>fund):
#             self.balance-=fund
#             return self.balance
#         else:
#             return "There is no sufficient fund and add more funds to withdrawl."
        
# B1=BankAccount(1000)
# print(f"After Deposite :{B1.deposit(500)}")
# print(f"After Withdrawl:{B1.withdrawl(200)}")
# print(f"{B1.withdrawl(2000)}")


"""
Write a Python program to create a Light class with three methods: turn_on() that switches the light on, turn_off() that switches it off, and status() that reports whether the light is currently on or off.
"""
# class Light:
#     def __init__(self):
#             self.light=False


#     def light_on(self):
#         self.light=True
#         return "ON"
    
#     def light_off(self):
#         self.light=False
#         return "Off"
    
#     def status(self):
#         if self.light==True:
#             return "Light-on"
#         else:
#             return "Light-off"
        
# l1=Light()
# print(l1.light_on())
# print(l1.status())
# print(l1.light_off())
# print(l1.status())


"""
Write a Python program to create a User class that stores a username and a password. Add a check_password(input_password) method that returns True if the input matches the stored password, and False otherwise.
"""
# class User:
#     def __init__(self, username, password):
#         self.username=username
#         self.password=password

#     def check_password(self, input_password):
#         if self.password==input_password:
#             return "TRUE - Password is correct"
#         else:
#             return "FALSE- Password is not correct"
        
# U1=User("Palak Yadav","p112a11")
# print(U1.check_password("p112a1"))


"""
Write a Python program to create a Temperature class that stores a temperature in Celsius. Add two methods: to_fahrenheit() that converts and returns the value in Fahrenheit, and to_kelvin() that converts and returns the value in Kelvin.
"""

# class Temperature:
#     def __init__(self,calcius):
#         self.calcius=calcius
    
#     def to_fahrenheit(self):
#         return (self.calcius * 18)+32
    
#     def to_kelvin(self):
#         return self.calcius+273.15
    

# T1=Temperature(32)
# print(f"Fahrenheit : {T1.to_fahrenheit()}")
# print(f"Kelvin : {T1.to_kelvin()}")

"""
Write a Python program to create a Notebook class that maintains an internal list of notes. Add an add_note(note) method that appends a new note to the list, and a show_notes() method that prints all stored notes.
"""
# class Notebook:
#     def __init__(self):
#         self.notes=[]

#     def add_notes(self,note):
#         self.notes.append(note)

#     def show_notes(self):
#         for i in range(len(self.notes)):
#             print(f"{i+1}. {self.notes[i]}")
        

# N1=Notebook()
# N1.add_notes("Math")
# N1.add_notes("physics")
# N1.add_notes("Chemistry")
# N1.show_notes()


"""
Write a Python program to create a CoffeeMachine class that tracks three resource attributes: water, coffee, and milk (in ml/g). Add a make_latte() method that checks whether sufficient resources are available, deducts them if so, and prints an appropriate message in either case.
"""

# class CoffeeMachine:
#     def __init__(self,water,coffee,milk):
#         self.water=water
#         self.coffee=coffee
#         self.milk=milk

#     def make_latte(self,water,coffee,milk):
#         if (self.water>=water) and (self.coffee>=coffee) and (self.milk>=milk):
#             remW=self.water-water
#             remC=self.coffee-coffee
#             remM=self.milk-milk
#             print(f"Latte Made : Remaining- Water :{remW}ml, Coffee : {remC}g and Milk : {remM}ml.")

#             if (remW >=water) and (remC>=coffee) and (remM>=milk):
#                 print("Can I make one more lattee !")
#             else:
#                 print("Not enought resources to make a lattee.")

# L1=CoffeeMachine(300,100,200)
# L1.make_latte(200,20,150)
# print("--------------------------")
# L1.make_latte(10,20,50)


"""
Write a Python program to create a Vehicle class with a class attribute color = "White" that is shared by all instances. Create two vehicle objects and demonstrate that both share the same default color, then show that changing the class attribute updates all instances that have not overridden it.
"""
        
# class Vechicle :
#     color="White"
#     def __init__(self,name,speed):
#         self.name=name
#         self.speed=speed
    


# V1=Vechicle("Tesla",200)
# V2=Vechicle("BMW",250)
# print(f"{V1.name}:- Color: {V1.color}, Speed: {V1.speed}")
# print(f"{V2.name}:- Color: {V2.color}, Speed: {V2.speed}")
# # print("------------------")
# Vechicle.color="Red"
# print(f"{V1.name}:- Color: {V1.color}, Speed: {V2.speed}")
# print(f"{V2.name}:- Color: {V2.color}, Speed: {V1.speed}")


"""
Write a Python program to create a Vehicle parent class with name and max_speed attributes and a display() method. Then create a Bus child class that inherits everything from Vehicle without adding anything new, and confirm that an instance of Bus can access the parent's method.
"""

# class Vechicle :
#     def __init__(self,name,max_speed):
#         self.name=name
#         self.max_speed=max_speed

#     def display(self):
#         print(f"Vechicle: {self.name}, Max_speed: {self.max_speed} km/hr.")

    

# class Bus(Vechicle):
#     pass

# B1=Bus("School Bus",120)
# B1.display()


"""
Write a Python program where a Vehicle parent class has a seating_capacity() method that accepts a capacity argument. Create a Bus child class that overrides this method to provide a default seating capacity of 50, using super() to call the parent's version internally.
"""

# class Vechicle:
#     def __init__(self,name,max_speed):
#         self.name=name
#         self.max_speed=max_speed

#     def seating_capacity(self,capacity):
#         print(f"{self.name} seating capacity is: {capacity}")

# class Bus(Vechicle):
#     def seating_capacity(self):
#         super().seating_capacity(50)
    

    
# B1=Bus("School Bus", 120)
# B1.seating_capacity()

"""
Write a Python program that creates a Vehicle parent class with a base fare, then extends a Taxi child class that adds a 10% maintenance fee on top of the base fare using super().
"""

# class Vechicle :
#     def __init__(self, name):
#         self.name=name

#     def base_fare(self,base_fare):
#         base_fare=base_fare+(base_fare*10)/100
#         print(f"Total fare with maintenance fee: {base_fare}")
        

# class Taxi(Vechicle):
#     def base_fare(self,base_fare):
#         super().base_fare(base_fare)


# n=int(input("Enter the base fare of the Taxi :"))
# T1=Taxi("OLa")
# T1.base_fare(n)


"""
Write a Python program that defines an Animal base class with a speak() method, then overrides it in Dog and Cat subclasses to return their respective sounds.
"""

