from abc import ABC, abstractmethod

# ============================================================
# INHERITANCE PROGRAMS
# ============================================================

# 1. Employee → Manager
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def annual_salary(self):
        return self.salary * 12

    def display(self):
        super().display()
        print(f"Department: {self.department}, Annual Salary: {self.annual_salary()}")


# 2. Vehicle → Car
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class Car(Vehicle):
    def __init__(self, brand, model, fuel_type, price):
        super().__init__(brand, model)
        self.fuel_type = fuel_type
        self.price = price

    def discounted_price(self, discount):
        return self.price - (self.price * discount / 100)

    def display(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Fuel: {self.fuel_type}, Price: {self.price}")


# 3. Academic + Sports → Student
class Academic:
    def __init__(self, marks):
        self.marks = marks


class Sports:
    def __init__(self, points):
        self.points = points


class Student(Academic, Sports):
    def __init__(self, marks, points):
        Academic.__init__(self, marks)
        Sports.__init__(self, points)

    def performance(self):
        return self.marks + self.points


# 5. Person → Student → ResearchStudent
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student2(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent(Student2):
    def __init__(self, name, age, roll_no, course, topic, guide):
        super().__init__(name, age, roll_no, course)
        self.topic = topic
        self.guide = guide

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Roll: {self.roll_no}, "
              f"Course: {self.course}, Topic: {self.topic}, Guide: {self.guide}")


# 6. BankAccount → SavingsAccount → PremiumSavingsAccount
class BankAccount:
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance


class SavingsAccount(BankAccount):
    def __init__(self, acc_no, balance, interest_rate):
        super().__init__(acc_no, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, acc_no, balance, interest_rate, bonus):
        super().__init__(acc_no, balance, interest_rate)
        self.bonus = bonus

    def calculate_interest(self):
        return super().calculate_interest() + self.bonus


# 7. Shape → Circle, Rectangle, Triangle
class Shape:
    def display_name(self):
        print("Shape")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# ============================================================
# POLYMORPHISM PROGRAMS
# ============================================================

# 1. Shape with polymorphic area()
class ShapePoly:
    def area(self):
        pass


class CirclePoly(ShapePoly):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class RectanglePoly(ShapePoly):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class TrianglePoly(ShapePoly):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# 9. Operator Overloading: Distance
class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        total_inches = self.inches + other.inches
        total_feet = self.feet + other.feet + total_inches // 12
        total_inches = total_inches % 12
        return Distance(total_feet, total_inches)

    def __str__(self):
        return f"{self.feet} ft {self.inches} in"


# ============================================================
# ABSTRACTION PROGRAMS
# ============================================================

# 1. Abstract Shape
class ShapeAbs(ABC):
    @abstractmethod
    def area(self):
        pass


class CircleAbs(ShapeAbs):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2


class RectangleAbs(ShapeAbs):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


class TriangleAbs(ShapeAbs):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# ============================================================
# DEMONSTRATION
# ============================================================

if __name__ == "__main__":
    print("\n--- Inheritance Demo ---")
    m = Manager(101, "Alice", 50000, "HR")
    m.display()

    c = Car("Toyota", "Corolla", "Petrol", 1000000)
    c.display()
    print("Discounted Price:", c.discounted_price(10))

    s = Student(80, 20)
    print("Performance:", s.performance())

    rs = ResearchStudent("Bob", 25, 12, "CS", "AI", "Dr. Smith")
    rs.display()

    sa = PremiumSavingsAccount(201, 10000, 5, 200)
    print("Interest:", sa.calculate_interest())

    print("Circle Area:", Circle(5).area())

    print("\n--- Polymorphism Demo ---")
    shapes = [CirclePoly(5), RectanglePoly(4, 6), TrianglePoly(3, 7)]
    for sh in shapes:
        print("Area:", sh.area())

    d1, d2 = Distance(5, 8), Distance(3, 10)
    print("Distance Sum:", d1 + d2)

    print("\n--- Abstraction Demo ---")
    abs_shapes = [CircleAbs(5), RectangleAbs(4, 6), TriangleAbs(3, 7)]
    for sh in abs_shapes:
        print("Area:", sh.area())
