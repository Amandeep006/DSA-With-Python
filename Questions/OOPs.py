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

class BankAccount:
    def __init__(self, balance):
        self.balance=balance
        
    
    def deposit(self,fund):
        self.balance+=fund
        return self.balance

    def withdrawl(self,fund):
        if (self.balance>fund):
            self.balance-=fund
            return self.balance
        else:
            return "There is no sufficient fund and add more funds to withdrawl."
        
B1=BankAccount(1000)
print(f"After Deposite :{B1.deposit(500)}")
print(f"After Withdrawl:{B1.withdrawl(200)}")
print(f"{B1.withdrawl(2000)}")
