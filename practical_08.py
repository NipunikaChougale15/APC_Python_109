#1
class Employee :
    def __init__(self,eid,name,sal):
        self.emp_id=eid
        self.name=name
        self.salary=sal
    def show(self):
        print("Details:")
        print("emp id:",self.emp_id)
        print("name:",self.name)
        print("salary:",self.salary)
class Manager(Employee):
    def __init__(self,eid,name,sal,dept):
        super().__init__(eid,name,sal)
        self.department=dept
    def display(self):
        self.show()
        print("Department:",self.department)
    def annaulsal(self):
        print("Annaul sal",self.salary*12)
        
m=Manager(101,"srushti",100000,"backend")
m.display()
m.annaulsal()
#2
class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def show(self):
        print("brand:",self.brand)
        print("model:",self.model)
class Car(Vehicle):
    def __init__(self,brand,model,fule_type,price):
        super().__init__(brand,model)
        self.fuel_type=fule_type
        self.price=price
    def display(self):
        self.show()
        print("fuel type:",self.fuel_type)
        print("price:",self.price)
    def discounted_price(self, discount):
        return self.price - (self.price * discount / 100)
car = Car("Toyota", "Fortuner", "Diesel", 3000000)
# Display details
car.display() # Calculate discounted price
discount= 10
print("Discount:", discount, "%")
print("Discounted Price: ₹",
car.discounted_price(discount))
#3
class Academic:
    def __init__(self, marks):
        self.marks = marks

    def academic_marks(self):
        return sum(self.marks)


class Sports:
    def __init__(self, sports_points):
        self.sports_points = sports_points


class Student(Academic, Sports):
    def __init__(self, name, marks, sports_points):
        Academic.__init__(self, marks)
        Sports.__init__(self, sports_points)
        self.name = name

    def overall_performance(self):
        total = self.academic_marks() + self.sports_points
        return total

    def display(self):
        print("Name:", self.name)
        print("Academic Marks:", self.academic_marks())
        print("Sports Points:", self.sports_points)
        print("Overall Performance:", self.overall_performance())


s = Student("Rahul", [80, 85, 90], 20)
s.display()
#4
class PersonalDetails:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class ProfessionalDetails:
    def __init__(self, emp_id, designation, salary):
        self.emp_id = emp_id
        self.designation = designation
        self.salary = salary


class Employee(PersonalDetails, ProfessionalDetails):
    def __init__(self, name, age, emp_id, designation, salary):
        PersonalDetails.__init__(self, name, age)
        ProfessionalDetails.__init__(self, emp_id, designation, salary)

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.emp_id)
        print("Designation:", self.designation)
        print("Salary: ₹", self.salary)


e = Employee("Priya", 25, 101, "Software Engineer", 50000)
e.display()
#5
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, research_topic, guide_name):
        super().__init__(name, age, roll_no, course)
        self.research_topic = research_topic
        self.guide_name = guide_name

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.research_topic)
        print("Guide Name:", self.guide_name)


r = ResearchStudent("Amit", 24, 101, "M.Tech", "Artificial Intelligence", "Dr. Sharma")
r.display()
#6
class BankAccount:
    def __init__(self, account_no, balance):
        self.account_no = account_no
        self.balance = balance


class SavingsAccount(BankAccount):
    def __init__(self, account_no, balance, interest_rate):
        super().__init__(account_no, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.balance * self.interest_rate / 100


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_no, balance, interest_rate, benefits):
        super().__init__(account_no, balance, interest_rate)
        self.benefits = benefits

    def display(self):
        print("Account Number:", self.account_no)
        print("Balance: ₹", self.balance)
        print("Interest Rate:", self.interest_rate, "%")
        print("Interest: ₹", self.calculate_interest())
        print("Benefits:", self.benefits)


account = PremiumSavingsAccount(
    12345, 50000, 6, "Free ATM and Priority Banking"
)

account.display()
#7
class Shape:
    def display_name(self):
        print("Shape:", self.__class__.__name__)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


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


c = Circle(7)
r = Rectangle(10, 5)
t = Triangle(10, 6)

c.display_name()
print("Area:", c.area())

r.display_name()
print("Area:", r.area())

t.display_name()
print("Area:", t.area())
#8
class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary


class Manager(Employee):
    def salary(self):
        allowance = self.basic_salary * 0.30
        return self.basic_salary + allowance

    def display(self):
        print("Manager:", self.name)
        print("Employee ID:", self.emp_id)
        print("Salary: ₹", self.salary())


class Developer(Employee):
    def salary(self):
        allowance = self.basic_salary * 0.20
        return self.basic_salary + allowance

    def display(self):
        print("Developer:", self.name)
        print("Employee ID:", self.emp_id)
        print("Salary: ₹", self.salary())


class Tester(Employee):
    def salary(self):
        allowance = self.basic_salary * 0.15
        return self.basic_salary + allowance

    def display(self):
        print("Tester:", self.name)
        print("Employee ID:", self.emp_id)
        print("Salary: ₹", self.salary())


m = Manager(101, "Rahul", 50000)
d = Developer(102, "Amit", 40000)
t = Tester(103, "Priya", 35000)

m.display()
d.display()
t.display()
#9
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no = roll_no


class Faculty(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject


class TeachingAssistant(Student, Faculty):
    def __init__(self, name, age, roll_no, subject):
        Person.__init__(self, name, age)
        self.roll_no = roll_no
        self.subject = subject

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Subject:", self.subject)


ta = TeachingAssistant("Neha", 23, 101, "Python")
ta.display()
#10
class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def display(self):
        print("Brand:", self.brand)


class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


class Bike(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model


class SportsCar(Car):
    def __init__(self, brand, model, speed):
        super().__init__(brand, model)
        self.speed = speed

    def display(self):
        print("Sports Car")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Speed:", self.speed, "km/h")


class ElectricBike(Bike):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def display(self):
        print("Electric Bike")
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Battery:", self.battery, "kWh")


car = SportsCar("BMW", "M4", 280)
bike = ElectricBike("Ola", "S1", 4)

car.display()
print()
bike.display()
#11
class Student:
    def __init__(self, roll_no, name, course):
        self.roll_no = roll_no
        self.name = name
        self.course = course


class Result(Student):
    def __init__(self, roll_no, name, course, marks):
        super().__init__(roll_no, name, course)
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / 3

    def grade(self):
        p = self.percentage()

        if p >= 90:
            return "A+"
        elif p >= 80:
            return "A"
        elif p >= 70:
            return "B"
        elif p >= 60:
            return "C"
        else:
            return "D"

    def display(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Course:", self.course)
        print("Total:", self.total())
        print("Percentage:", self.percentage(), "%")
        print("Grade:", self.grade())


r = Result(101, "Sneha", "B.Tech", [85, 90, 80])
r.display()
#12
class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id
        self.name = name
        self.price = price


class ElectronicProduct(Product):
    def __init__(self, product_id, name, price, brand, warranty):
        super().__init__(product_id, name, price)
        self.brand = brand
        self.warranty = warranty

    def final_price(self, discount):
        return self.price - (self.price * discount / 100)

    def display(self):
        print("Product ID:", self.product_id)
        print("Name:", self.name)
        print("Brand:", self.brand)
        print("Warranty:", self.warranty, "years")
        print("Original Price: ₹", self.price)
        print("Final Price: ₹", self.final_price(10))


p = ElectronicProduct(101, "Laptop", 60000, "HP", 2)
p.display()
#13
class Printer:
    def print_document(self):
        print("Printing document...")


class Scanner:
    def scan_document(self):
        print("Scanning document...")


class MultifunctionDevice(Printer, Scanner):
    def display(self):
        print("Multifunction Device")
        self.print_document()
        self.scan_document()


device = MultifunctionDevice()
device.display()
#14
class Camera:
    def take_photo(self):
        print("Photo taken successfully.")


class Phone:
    def make_call(self, number):
        print("Calling", number)


class Smartphone(Camera, Phone):
    def display(self):
        print("Smartphone supports:")
        self.take_photo()
        self.make_call("9876543210")


phone = Smartphone()
phone.display()
#15
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, roll_no, course):
        super().__init__(name, age)
        self.roll_no = roll_no
        self.course = course


class ResearchStudent(Student):
    def __init__(self, name, age, roll_no, course, research_topic, guide_name):
        super().__init__(name, age, roll_no, course)
        self.research_topic = research_topic
        self.guide_name = guide_name

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll No:", self.roll_no)
        print("Course:", self.course)
        print("Research Topic:", self.research_topic)
        print("Guide Name:", self.guide_name)


student = ResearchStudent(
    "Riya", 24, 101, "M.Tech",
    "Machine Learning", "Dr. Patil"
)

student.display()
#16
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating.")


class Dog(Animal):
    def sound(self):
        print(self.name, "says Woof!")


class Cat(Animal):
    def sound(self):
        print(self.name, "says Meow!")


class Cow(Animal):
    def sound(self):
        print(self.name, "says Moo!")


dog = Dog("Tommy")
cat = Cat("Kitty")
cow = Cow("Gauri")

dog.eat()
dog.sound()

cat.eat()
cat.sound()

cow.eat()
cow.sound()
#17
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating.")


class Dog(Animal):
    def sound(self):
        print(self.name, "says Woof!")


class Cat(Animal):
    def sound(self):
        print(self.name, "says Meow!")


class Cow(Animal):
    def sound(self):
        print(self.name, "says Moo!")


dog = Dog("Tommy")
cat = Cat("Kitty")
cow = Cow("Gauri")

dog.eat()
dog.sound()

cat.eat()
cat.sound()

cow.eat()
cow.sound()
#17
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "is eating.")


class Dog(Animal):
    def sound(self):
        print(self.name, "says Woof!")


class Cat(Animal):
    def sound(self):
        print(self.name, "says Meow!")


class Cow(Animal):
    def sound(self):
        print(self.name, "says Moo!")


dog = Dog("Tommy")
cat = Cat("Kitty")
cow = Cow("Gauri")

dog.eat()
dog.sound()

cat.eat()
cat.sound()

cow.eat()
cow.sound()
#18
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization

    def display_doctor(self):
        self.display_person()
        print("Specialization:", self.specialization)


class Patient(Person):
    def __init__(self, name, age, disease):
        super().__init__(name, age)
        self.disease = disease

    def display_patient(self):
        self.display_person()
        print("Disease:", self.disease)


class Surgeon(Doctor):
    def surgery(self):
        print("Surgeon performs surgery.")


class MedicalResearcher(Doctor):
    def research(self):
        print("Medical researcher performs medical research.")


surgeon = Surgeon("Dr. Rahul", 40, "General Surgery")
researcher = MedicalResearcher("Dr. Priya", 38, "Medical Research")
patient = Patient("Amit", 25, "Fever")

print("--- Surgeon ---")
surgeon.display_doctor()
surgeon.surgery()

print("\n--- Medical Researcher ---")
researcher.display_doctor()
researcher.research()

print("\n--- Patient ---")
patient.display_patient()
#####polymorphism
# ============================================================
# 1
# Runtime Polymorphism - Shape
# ============================================================

class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


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


shapes = [Circle(5), Rectangle(10, 5), Triangle(10, 6)]

for shape in shapes:
    print("Area:", shape.area())


# ============================================================
# 2
# Runtime Polymorphism - Employee Salary
# ============================================================

class Employee:
    def calculate_salary(self):
        pass


class Manager(Employee):
    def calculate_salary(self):
        return 50000 + 15000


class Developer(Employee):
    def calculate_salary(self):
        return 40000 + 8000


class Tester(Employee):
    def calculate_salary(self):
        return 35000 + 5000


employees = [Manager(), Developer(), Tester()]

for employee in employees:
    print("Salary: Rs.", employee.calculate_salary())


# ============================================================
# 3
# Runtime Polymorphism - Vehicle
# ============================================================

class Vehicle:
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car starts with a key.")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with a self-start button.")


class Bus(Vehicle):
    def start(self):
        print("Bus starts with an ignition key.")


vehicles = [Car(), Bike(), Bus()]

for vehicle in vehicles:
    vehicle.start()


# ============================================================
# 4
# Runtime Polymorphism - Animal
# ============================================================

class Animal:
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        print("Dog says Woof!")


class Cat(Animal):
    def sound(self):
        print("Cat says Meow!")


class Cow(Animal):
    def sound(self):
        print("Cow says Moo!")


class Lion(Animal):
    def sound(self):
        print("Lion says Roar!")


animals = [Dog(), Cat(), Cow(), Lion()]

for animal in animals:
    animal.sound()


# ============================================================
# 5
# Runtime Polymorphism - Notification
# ============================================================

class Notification:
    def send(self):
        pass


class EmailNotification(Notification):
    def send(self):
        print("Sending notification through Email.")


class SMSNotification(Notification):
    def send(self):
        print("Sending notification through SMS.")


class PushNotification(Notification):
    def send(self):
        print("Sending notification through Push Notification.")


notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification()
]

for notification in notifications:
    notification.send()


# ============================================================
# 6
# Runtime Polymorphism - Student Grade
# ============================================================

class Student:
    def calculate_grade(self, marks):
        pass


class EngineeringStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 85:
            return "A"
        elif marks >= 70:
            return "B"
        elif marks >= 50:
            return "C"
        else:
            return "F"


class MedicalStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        elif marks >= 60:
            return "C"
        else:
            return "F"


class ManagementStudent(Student):
    def calculate_grade(self, marks):
        if marks >= 80:
            return "A"
        elif marks >= 65:
            return "B"
        elif marks >= 50:
            return "C"
        else:
            return "F"


students = [
    EngineeringStudent(),
    MedicalStudent(),
    ManagementStudent()
]

for student in students:
    print("Grade:", student.calculate_grade(80))


# ============================================================
# 7
# Runtime Polymorphism - Bank Account
# ============================================================

class BankAccount:
    def calculate_interest(self, balance):
        pass


class SavingsAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.06


class CurrentAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.02


class FixedDepositAccount(BankAccount):
    def calculate_interest(self, balance):
        return balance * 0.08


accounts = [
    SavingsAccount(),
    CurrentAccount(),
    FixedDepositAccount()
]

for account in accounts:
    print("Interest: Rs.", account.calculate_interest(50000))


# ============================================================
# 8
# Runtime Polymorphism - Report
# ============================================================

class Report:
    def generate(self):
        pass


class PDFReport(Report):
    def generate(self):
        print("Generating PDF Report.")


class ExcelReport(Report):
    def generate(self):
        print("Generating Excel Report.")


class HTMLReport(Report):
    def generate(self):
        print("Generating HTML Report.")


def generate_report(report):
    report.generate()


generate_report(PDFReport())
generate_report(ExcelReport())
generate_report(HTMLReport())


# ============================================================
# 9
# Operator Overloading - Distance
# ============================================================

class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __add__(self, other):
        total_inches = self.inches + other.inches
        feet = self.feet + other.feet

        feet += total_inches // 12
        inches = total_inches % 12

        return Distance(feet, inches)

    def display(self):
        print(self.feet, "feet", self.inches, "inches")


d1 = Distance(5, 8)
d2 = Distance(3, 7)

d3 = d1 + d2

print("First Distance:")
d1.display()

print("Second Distance:")
d2.display()

print("Total Distance:")
d3.display()


# ============================================================
# 10
# Operator Overloading - Student Comparison
# ============================================================

class Student10:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __gt__(self, other):
        return self.marks > other.marks

    def __lt__(self, other):
        return self.marks < other.marks


s1 = Student10("Rahul", 85)
s2 = Student10("Priya", 90)

print("s1 > s2:", s1 > s2)
print("s1 < s2:", s1 < s2)


# ============================================================
# 11
# Operator Overloading - Product Comparison
# ============================================================

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price


p1 = Product("Laptop", 60000)
p2 = Product("Mobile", 30000)

print("Products have equal price:", p1 == p2)
print("Laptop price greater than Mobile:", p1 > p2)


# ============================================================
# 12
# Polymorphism - Online Shopping Payment
# ============================================================

class Payment:
    def make_payment(self, amount):
        pass


class UPIPayment(Payment):
    def make_payment(self, amount):
        print("UPI Payment of Rs.", amount, "successful.")


class CardPayment(Payment):
    def make_payment(self, amount):
        print("Card Payment of Rs.", amount, "successful.")


class WalletPayment(Payment):
    def make_payment(self, amount):
        print("Wallet Payment of Rs.", amount, "successful.")


def process_payment(payment, amount):
    payment.make_payment(amount)


process_payment(UPIPayment(), 1000)
process_payment(CardPayment(), 2000)
process_payment(WalletPayment(), 1500)


# ============================================================
# 13
# Runtime Polymorphism - Person Roles
# ============================================================

class Person:
    def display_role(self):
        pass


class Student13(Person):
    def display_role(self):
        print("Role: Student")


class Faculty(Person):
    def display_role(self):
        print("Role: Faculty")


class Administrator(Person):
    def display_role(self):
        print("Role: Administrator")


people = [
    Student13(),
    Faculty(),
    Administrator()
]

for person in people:
    person.display_role()


# ============================================================
# 14
# Runtime Polymorphism - Media
# ============================================================

class Media:
    def play(self):
        pass


class Audio(Media):
    def play(self):
        print("Playing Audio.")


class Video(Media):
    def play(self):
        print("Playing Video.")


class Podcast(Media):
    def play(self):
        print("Playing Podcast.")


media_list = [
    Audio(),
    Video(),
    Podcast()
]

for media in media_list:
    media.play()


# ============================================================
# 15
# Runtime Polymorphism - Smart Devices
# ============================================================

class SmartDevice:
    def turn_on(self):
        pass

    def turn_off(self):
        pass


class Light(SmartDevice):
    def turn_on(self):
        print("Light is turned ON.")

    def turn_off(self):
        print("Light is turned OFF.")


class Fan(SmartDevice):
    def turn_on(self):
        print("Fan is turned ON.")

    def turn_off(self):
        print("Fan is turned OFF.")


class AC(SmartDevice):
    def turn_on(self):
        print("AC is turned ON.")

    def turn_off(self):
        print("AC is turned OFF.")


class TV(SmartDevice):
    def turn_on(self):
        print("TV is turned ON.")

    def turn_off(self):
        print("TV is turned OFF.")


devices = [
    Light(),
    Fan(),
    AC(),
    TV()
]

for device in devices:
    device.turn_on()
    device.turn_off()

###Abstraction
#1
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Circle(Shape):
    def area(self,r):
        return 3.14*r*r
class Rectangle(Shape):
    def area(self,l,b):
        return l*b
class Traingle(Shape):
    def area(self,ba,ht):
        return 0.5*ba*ht
c=Circle()
r=Rectangle()
t=Traingle()
print("Area of circle:",c.area(2))
print("Area of Rectangle:",r.area(2,3))
print("Area of Traingle:",t.area(2,5))
#2
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass
class Car(Vehicle):
    def start(self):
        print("car started")
    def stop(self):
        print("car stopped")
class Bike(Vehicle):
    def start(self):
        print("Bike started")
    def stop(self):
        print("Bike stopped")
class Bus(Vehicle):
    def start(self):
        print("Bus started")
    def stop(self):
        print("Bus stopped")
c=Car()
b=Bike()
bus=Bus()
print("Car start:")
c.start()

print("Car stop:")
c.stop()

print("Bike start:")
b.start()

print("Bike stop:")
b.stop()

print("Bus start:")
bus.start()

print("Bus stop:")
bus.stop()


# 3

class BankAccount(ABC):
    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Savings deposit:", amount)
        print("Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Savings withdrawal:", amount)
            print("Balance:", self.balance)
        else:
            print("Insufficient balance")


class CurrentAccount(BankAccount):
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Current deposit:", amount)
        print("Balance:", self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Current withdrawal:", amount)
            print("Balance:", self.balance)
        else:
            print("Insufficient balance")


s = SavingsAccount(10000)
s.deposit(2000)
s.withdraw(3000)

c = CurrentAccount(20000)
c.deposit(5000)
c.withdraw(4000)


# 4

class FoodOrder(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass


class RestaurantOrder(FoodOrder):
    def calculate_bill(self):
        return 500

    def delivery_charge(self):
        return 0


class HomeDeliveryOrder(FoodOrder):
    def calculate_bill(self):
        return 500

    def delivery_charge(self):
        return 50


r = RestaurantOrder()
h = HomeDeliveryOrder()

print("Restaurant Bill:", r.calculate_bill() + r.delivery_charge())
print("Home Delivery Bill:", h.calculate_bill() + h.delivery_charge())


# 5

class Patient(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def treatment(self):
        pass


class InPatient(Patient):
    def calculate_bill(self):
        return 5000

    def treatment(self):
        print("InPatient: Hospital admission and treatment")


class OutPatient(Patient):
    def calculate_bill(self):
        return 1000

    def treatment(self):
        print("OutPatient: Doctor consultation")


class EmergencyPatient(Patient):
    def calculate_bill(self):
        return 10000

    def treatment(self):
        print("EmergencyPatient: Emergency treatment")


p1 = InPatient()
p2 = OutPatient()
p3 = EmergencyPatient()

print("InPatient Bill:", p1.calculate_bill())
p1.treatment()

print("OutPatient Bill:", p2.calculate_bill())
p2.treatment()

print("EmergencyPatient Bill:", p3.calculate_bill())
p3.treatment()


# 6

class Transport(ABC):
    @abstractmethod
    def calculate_fare(self, distance):
        pass


class Bus(Transport):
    def calculate_fare(self, distance):
        return distance * 10


class Train(Transport):
    def calculate_fare(self, distance):
        return distance * 5


class Taxi(Transport):
    def calculate_fare(self, distance):
        return distance * 20


class Flight(Transport):
    def calculate_fare(self, distance):
        return distance * 50


distance = 100

bus = Bus()
train = Train()
taxi = Taxi()
flight = Flight()

print("Bus Fare:", bus.calculate_fare(distance))
print("Train Fare:", train.calculate_fare(distance))
print("Taxi Fare:", taxi.calculate_fare(distance))
print("Flight Fare:", flight.calculate_fare(distance))


# 7

class Question(ABC):
    @abstractmethod
    def evaluate_answer(self):
        pass


class MCQQuestion(Question):
    def __init__(self, answer):
        self.answer = answer

    def evaluate_answer(self):
        if self.answer == "B":
            return "Correct Answer"
        else:
            return "Wrong Answer"


class TrueFalseQuestion(Question):
    def __init__(self, answer):
        self.answer = answer

    def evaluate_answer(self):
        if self.answer == True:
            return "Correct Answer"
        else:
            return "Wrong Answer"


class DescriptiveQuestion(Question):
    def __init__(self, answer):
        self.answer = answer

    def evaluate_answer(self):
        if len(self.answer) > 10:
            return "Answer Accepted"
        else:
            return "Answer Too Short"


q1 = MCQQuestion("B")
q2 = TrueFalseQuestion(True)
q3 = DescriptiveQuestion("Python is an object oriented language")

print(q1.evaluate_answer())
print(q2.evaluate_answer())
print(q3.evaluate_answer())


# 8

class Authentication(ABC):
    @abstractmethod
    def authenticate(self):
        pass


class PasswordAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using Password")


class OTPAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using OTP")


class BiometricAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using Biometric")


a1 = PasswordAuthentication()
a2 = OTPAuthentication()
a3 = BiometricAuthentication()

a1.authenticate()
a2.authenticate()
a3.authenticate()


# 9

class CloudStorage(ABC):
    @abstractmethod
    def upload_file(self):
        pass

    @abstractmethod
    def download_file(self):
        pass

    @abstractmethod
    def delete_file(self):
        pass


class GoogleDrive(CloudStorage):
    def upload_file(self):
        print("File uploaded to Google Drive")

    def download_file(self):
        print("File downloaded from Google Drive")

    def delete_file(self):
        print("File deleted from Google Drive")


class OneDrive(CloudStorage):
    def upload_file(self):
        print("File uploaded to OneDrive")

    def download_file(self):
        print("File downloaded from OneDrive")

    def delete_file(self):
        print("File deleted from OneDrive")


class Dropbox(CloudStorage):
    def upload_file(self):
        print("File uploaded to Dropbox")

    def download_file(self):
        print("File downloaded from Dropbox")

    def delete_file(self):
        print("File deleted from Dropbox")


g = GoogleDrive()
o = OneDrive()
d = Dropbox()

g.upload_file()
g.download_file()
g.delete_file()

o.upload_file()
o.download_file()
o.delete_file()

d.upload_file()
d.download_file()
d.delete_file()


# 10

class Appointment(ABC):
    @abstractmethod
    def book_appointment(self):
        pass

    @abstractmethod
    def calculate_fee(self):
        pass


class GeneralAppointment(Appointment):
    def book_appointment(self):
        print("General appointment booked")

    def calculate_fee(self):
        return 500


class SpecialistAppointment(Appointment):
    def book_appointment(self):
        print("Specialist appointment booked")

    def calculate_fee(self):
        return 1000


class EmergencyAppointment(Appointment):
    def book_appointment(self):
        print("Emergency appointment booked")

    def calculate_fee(self):
        return 2000


a1 = GeneralAppointment()
a2 = SpecialistAppointment()
a3 = EmergencyAppointment()

a1.book_appointment()
print("Fee:", a1.calculate_fee())

a2.book_appointment()
print("Fee:", a2.calculate_fee())

a3.book_appointment()
print("Fee:", a3.calculate_fee())


































        
        

        
