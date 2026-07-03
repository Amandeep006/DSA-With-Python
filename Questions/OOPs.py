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

# class Animals:
#     def speak(self):
#         print("Animals make a sound")

# class Dog(Animals):
#     def speak(self):
#         print("Dog says: Woof!")

# class Cat(Animals):
#     def speak(self):
#         print("Cat says: Meow!")

# dog=Dog()
# cat=Cat()
# dog.speak()
# cat.speak()


"""
Write a Python program that defines an Employee base class, then creates FullTimeEmployee and PartTimeEmployee subclasses, each implementing different pay calculation logic.
"""
# class Employee:
#     def __init__(self,name):
#         self.name=name
    
#     def salary(self):
#         return 0

# class FullTimeEmployee(Employee):
#     def __init__(self,name,pay):
#         super().__init__(name)
#         self.pay=pay

#     def salary(self):
#         return self.pay/12

# class PartTimeEmployee(Employee):
#     def __init__(self,name,hr_rate,hr_worked):
#         super().__init__(name)
#         self.hr_rate=hr_rate
#         self.hr_worked=hr_worked

#     def salary(self):
#         return self.hr_rate*self.hr_worked

# ft=FullTimeEmployee("Alice",60000)
# pt=PartTimeEmployee("Bob",500,20)


# print(f"{ft.name}'s monthly pay: {ft.salary()}")
# print(f"{pt.name}'s monthly pay: {pt.salary()}")


"""
Write a Python program that defines a Shape base class with an area() method, then implements it in Circle, Square, and Triangle subclasses using the appropriate geometric formulas.
"""

# class Shape:
#     def Area(self):
#         return 0

# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius=radius

#     def Area(self):
#         return (3.14*self.radius*self.radius)
    
# class Square(Shape):
#     def __init__(self,side):
#         self.side=side

#     def Area(self):
#         return (self.side*self.side)

# class Triangle(Shape):
#     def __init__(self,base,height):
#         self.base=base
#         self.height=height

#     def Area(self):
#         return (self.base*self.height)/2
    
# circle=Circle(7)
# square=Square(4)
# triangle=Triangle(6,8)

# print(f"Circle area: {circle.Area()}")
# print(f"Square area : {square.Area()}")
# print(f"Triangle area : {triangle.Area()}")


"""
Write a Python program that defines a Media base class, then creates Book, Magazine, and DVD subclasses, each with type-specific attributes and a describe() method.
"""

# class MediaBase:
    
#     def __init__(self,name,price,des):
#         self.name=name
#         self.price=price
#         self.des=des

    
# class Book(MediaBase):    
#     def desc(self):
#         return self.des

# class Magazine(MediaBase):
#     def des(self):
#         return self.des
    
# class DVD(MediaBase):
#     def des(self):
#         return self.des

# book=Book("clean code",499,"Robert C. Martin")
# magazine=Magazine("Wired",150,"Monthly")
# dvd=DVD("Inception",299,148)

# print(f"Book: {book.name} by {book.des} - Rs.{book.price}")
# print(f"Magazine: {magazine.name} by {magazine.des} - Rs.{magazine.price}")
# print(f"DVD: {dvd.name} by {dvd.des} - Rs.{dvd.price}")


"""
Write a Python program that creates an Order class with a total amount, then creates a DiscountedOrder subclass that applies a 10% discount to the total.
"""

# class Order:
#     def __init__(self,order_ID):
#         self.order_ID=order_ID
       

# class DiscountedOrder(Order):
#     def __init__(self, order_id,total_amount):
#         super().__init__(order_id)
#         self.total_amount=total_amount
    
#     def discount(self):
#         self.total_amount-=(self.total_amount*10)/100
#         return self.total_amount


# do=DiscountedOrder("ORD001",1200)
# print(f"Order ID: {do.order_ID}")
# print(f"Original Total: {do.total_amount}")
# print(f"Discounted Total: {do.discount()}")    



"""
Write a Python program that defines a Vehicle base class and creates Bike, Truck, and Bus subclasses, each defining a unique max_speed attribute and a describe() method.
"""

# class Vechicle:
#     def __init__(self, name,max_speed):
#         self.name=name
#         self.max_speed=max_speed

#     def desc(self,des):
#         self.des=des
#         return self.des

# class Bike(Vechicle):
#     def __init__(self,name,max_speed):
#         super().__init__(name,max_speed)

#         print(f"Bike max speed: {self.max_speed} km/h")

#     def desc(self,des):
#         self.des=des
#         return self.des
        

# class Truck(Vechicle):
#     def __init__(self,name,max_speed):
#         super().__init__(name,max_speed)

#         print(f"Truck max speed: {self.max_speed} km/h")

#     def desc(self,des):
#         self.des=des
#         return self.des
    

# class Bus(Vechicle):
#     def __init__(self,name,max_speed):
#         super().__init__(name,max_speed)

#         print(f"Bus max speed: {self.max_speed} km/h")

#     def desc(self,des):
#         self.des=des
#         return self.des
        

# Bike("Bike",120)
# Truck("Truck",90)
# Bus("Bus",100)


"""
Write a Python program that creates objects from multiple classes and uses the built-in type() function to identify which class each object belongs to.
"""

# class Dog:
#     def ret(self):
#          return "Dog"
# class Cat:
#     def ret(self):
#         return "Cat"
# class Vechicle:
#     def ret(self):
#         return "Vechicle"

# d=Dog()
# c=Cat()
# v=Vechicle()

# print(f"d is of type: {type(d).__name__}")
# print(f"c is of type: {type(c).__name__}")
# print(f"v is of type: {type(v).__name__}")

# type(obj): Returns the class (type object) that obj was created from. For example, type(d) returns <class '__main__.Dog'>.
# type(obj).__name__: The .__name__ attribute on the returned type object gives just the plain string name of the class, such as "Dog", without the module prefix.

# class Dog:
#     pass

# class Cat:
#     pass

# class Vehicle:
#     pass

# d = Dog()
# c = Cat()
# v = Vehicle()

# objects = {"d": d, "c": c, "v": v}

# for name, obj in objects.items():
#     print(f"{name} is of type: {type(obj).__name__}")


"""
Write a Python program that uses isinstance() to check whether an object is an instance of a given class, and issubclass() to check whether one class is a subclass of another.
"""

# class Animal:
#     pass

# class Dog(Animal):
#     pass

# d=Dog()

# print("Is d an instance of Dog?", isinstance(d, Dog))
# print("Is d an instance of Animal?", isinstance(d, Animal))
# print("Is Dog a subclass of Animal?", issubclass(Dog, Animal))
# print("Is Animal a subclass of Dog?", issubclass(Animal, Dog))



"""
Write a Python program that creates a Vector class representing a 2D vector, and implements the __add__ dunder method so that two Vector objects can be added using the + operator.
"""
# __add__(self, other): Python calls this method automatically when the + operator is used between two Vector objects. self is the left operand and other is the right.

# __repr__: Defines the string representation of the object used by print() and the interactive shell. Without it, print(result) would display something like <__main__.Vector object at 0x...>.


# class Vector:
#     def __init__(self,x,y):
#         self.x=x
#         self.y=y

#     def __add__(self,other):
#         return Vector(self.x+other.x,self.y+other.y)
    
#     def __repr__(self):
#         return f"Vector({self.x},{self.y})"
     
    

# V1=Vector(2,3)
# V2=Vector(4,1)

# v=V1+V2
# print(v)


"""
Write a Python program that creates a Cart class that stores a list of items, and implements __len__ so that calling len(cart) returns the number of items currently in the cart.
"""

# class Cart:
#     def __init__(self,lst_items):
#         self.lst_items=lst_items

#     def __len__(self):
#         return len(self.lst_items)
    

# C1=Cart(['Apple','Banana','Mango'])
# print(f"Number of items in cart: {len(C1)}")


"""
Write a Python program that creates a BankAccount class where the balance is stored as a private attribute __balance, and exposed safely through a @property getter and a setter that validates the value before updating it.
"""
# class BankAccount:
    
#     def __init__(self,balance):
#         self.__balance=balance

#     @property
#     def balance(self):
#         return self.__balance

#     @balance.setter
#     def balance(self, amount):
#         if amount < 0:
#             print("Invalid balance. Must be non-negative.")
#         else:
#             self.__balance = amount

#     def deposite(self,amount):
#         self.balance=self.__balance+amount
    

# B1=BankAccount(1000)
# print(B1.balance)
# B1.deposite(500)
# print(B1.balance)

# B1.balance=-200


"""
Write a Python program that creates a Multiplier class which stores a factor, and implements __call__ so that an instance of the class can be invoked directly like a function to multiply a given number by that factor.
"""
# self.factor: Stores the multiplier value at construction time. This is the state that distinguishes callable objects from plain functions: the object remembers its configuration between calls.
# __call__(self, value): Python invokes this method whenever the object is called using parentheses, such as triple(10). Without this method, doing so would raise a TypeError: 'Multiplier' object is not callable.


# class Multiplier:
#     def __init__(self,factor):
#         self.factor=factor

#     def __call__(self,value):
#         return self.factor*value
    

# M1=Multiplier(3)
# M2=Multiplier(5)

# print(M1(10))
# print(M2(7))


"""
Write a Python program that creates a Passenger class and a Flight class. The Flight class should manage a list of Passenger objects and block further bookings when the seat capacity is reached.
"""

# class Passenger:
#     def __init__(self,name):
#         self.name=name

# class Flight:
#     def __init__(self,flight,capacity):
#         self.flight=flight
#         self.capacity=capacity
#         self.passengers=[]      
        

#     def Booked(self,passengers):
#         if len(self.passengers)< self.capacity:
#             print(f"{passengers.name} booked on Flight AI202.")
#         else:
#             print("Flight AI202 is fulled.")

# flight=Flight("Ai202",2)
# flight.Booked(Passenger("Alice"))
# flight.Booked(Passenger("Bob"))
# flight.Booked(Passenger("Charlie"))
# flight.Booked(Passenger("Alex"))



"""
   Write a Python program that defines an Animal base class with an eat() method, creates a few subclasses with their own eat() implementations, and builds a Zoo class that holds a list of animals and calls eat() on all of them via a feed_all() method.
"""  

# class Animals:
#     def eat(self):
#         return "eating"

# class Lion(Animals):
#      def eat(self):
#         return "Lion eats meat."

# class Elephant(Animals):
#      def eat(self):
#         return "Elephants eats grass."
    
# class Parrot(Animals):
#      def eat(self):
#         return "Parrot eats seeds."
    
# class ZOO:
#     def __init__(self):
#         self.animals=[]

#     def add_animal(self,animal):
#         self.animals.append(animal)
    
#     def feed_all(self):
#         for animal in self.animals:
#             print(animal.eat())


# zoo=ZOO()
# zoo.add_animal(Lion())
# zoo.add_animal(Elephant())
# zoo.add_animal(Parrot())
    
# zoo.feed_all()
        

"""
Write a Python program that creates a Character class with health, exp, and level attributes. The character should automatically level up and reset exp whenever accumulated experience reaches or exceeds 100.
"""

# class Character:
#     def __init__(self, name, health):
#         self.name = name
#         self.health = health
#         self.exp = 0
#         self.level = 1

#     def gain_exp(self, amount):
#         self.exp += amount
#         if self.exp >= 100:
#             self.exp -= 100
#             self.level += 1
#             print(f"{self.name} gained {amount} exp. Level up! Now Level {self.level}. (Remaining exp: {self.exp})")
#         else:
#             print(f"{self.name} gained {amount} exp. (Total: {self.exp})")

# hero = Character("Aria", health=100)
# hero.gain_exp(60)
# hero.gain_exp(60)

"""
Write a Python program that defines a Song class and a Playlist class. The Playlist should support adding songs, removing songs by title, and shuffling the order of the playlist randomly.
"""
import random
class Songs:
    def song(self):
        return "songs"

class Playlist:
    def __init__(self):
        self.songs=[]

    def add_songs(self,title):
        self.songs.append(title)
        return self.songs
    
    def remove_songs(self,title):
        self.songs.remove(title)
        return title

    def shuffle(self):
        random.shuffle(self.songs)
        print(f"After Shuffle: (Order will vary) : {self.songs}")


P1=Playlist()
P1.add_songs("Blinding Lights")
P1.add_songs("Levitating")
P1.add_songs("Peaches")
print(f"Playlist: {P1.songs}")
print(f"Removed: {P1.remove_songs("Levitating")}")
P1.shuffle()