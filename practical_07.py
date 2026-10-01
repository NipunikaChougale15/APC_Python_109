#1
class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        total = sum(self.marks)
        percentage = total / len(self.marks)

        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print("Percentage:", percentage, "%")
        print()


s1 = Student(1, "Rahul", [80, 75, 90, 85, 70])
s2 = Student(2, "Priya", [85, 88, 92, 80, 90])

s1.display()
s2.display()
#2
class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_hra(self):
        return self.basic_salary * 0.20

    def calculate_da(self):
        return self.basic_salary * 0.10

    def gross_salary(self):
        return self.basic_salary + self.calculate_hra() + self.calculate_da()

    def display(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Basic Salary:", self.basic_salary)
        print("HRA:", self.calculate_hra())
        print("DA:", self.calculate_da())
        print("Gross Salary:", self.gross_salary())


e = Employee(101, "Amit", 30000)
e.display()
#3
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


r = Rectangle(10, 5)

print("Length:", r.length)
print("Breadth:", r.breadth)
print("Area:", r.area())
print("Perimeter:", r.perimeter())
#4
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius


c = Circle(7)

print("Radius:", c.radius)
print("Area:", c.area())
print("Circumference:", c.circumference())
#5
class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print()


b1 = Book(101, "Python Programming", "John", 500)
b2 = Book(102, "Java Programming", "James", 600)
b3 = Book(103, "Data Structures", "Robert", 450)

b1.display()
b2.display()
b3.display()
#6
class ElectricityBill:
    def __init__(self, consumer_no, consumer_name, units):
        self.consumer_no = consumer_no
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):
        if self.units <= 100:
            bill = self.units * 5
        elif self.units <= 200:
            bill = (100 * 5) + ((self.units - 100) * 7)
        else:
            bill = (100 * 5) + (100 * 7) + ((self.units - 200) * 10)

        return bill

    def display(self):
        print("Consumer Number:", self.consumer_no)
        print("Consumer Name:", self.consumer_name)
        print("Units Consumed:", self.units)
        print("Electricity Bill: ₹", self.calculate_bill())


e = ElectricityBill(1001, "Suresh", 250)
e.display()
#7
class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Storage:", self.storage)
        print("Price: ₹", self.price)

    def discounted_price(self, discount):
        return self.price - (self.price * discount / 100)


m = MobilePhone("Samsung", "Galaxy A55", "128 GB", 30000)

m.display()
print("Price after 10% discount: ₹", m.discounted_price(10))
#8
class Patient:
    def __init__(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def display(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Consultation Fee: ₹", self.consultation_fee)

    def total_bill(self, medicine_fee):
        return self.consultation_fee + medicine_fee


p = Patient(101, "Riya", 25, "Fever", 500)

p.display()
print("Total Bill: ₹", p.total_bill(300))
#9
class ATM:
    def __init__(self, account_no, name, balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance

    def check_balance(self):
        print("Current Balance: ₹", self.balance)

    def deposit(self, amount):
        self.balance += amount
        print("Amount Deposited: ₹", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount Withdrawn: ₹", amount)
        else:
            print("Insufficient Balance")

    def account_details(self):
        print("Account Number:", self.account_no)
        print("Account Holder:", self.name)
        print("Balance: ₹", self.balance)


atm = ATM(12345, "Anita", 10000)

while True:
    print("\n--- ATM MENU ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Display Account Details")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        atm.check_balance()

    elif choice == 2:
        amount = float(input("Enter amount to deposit: "))
        atm.deposit(amount)

    elif choice == 3:
        amount = float(input("Enter amount to withdraw: "))
        atm.withdraw(amount)

    elif choice == 4:
        atm.account_details()

    elif choice == 5:
        print("Thank you for using ATM")
        break

    else:
        print("Invalid Choice")
        
#10
class Vehicle:
    def __init__(self, vehicle_no, model, rental_rate):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rental_rate = rental_rate
        self.available = True

    def rent(self):
        if self.available:
            self.available = False
            print("Vehicle rented successfully.")
        else:
            print("Vehicle is not available.")

    def return_vehicle(self):
        self.available = True
        print("Vehicle returned successfully.")

    def rental_charges(self, days):
        return self.rental_rate * days

    def display(self):
        print("Vehicle Number:", self.vehicle_no)
        print("Model:", self.model)
        print("Rental Rate:", self.rental_rate)
        print("Available:", self.available)


v = Vehicle("MH12AB1234", "Swift", 1500)

v.display()

v.rent()

days = int(input("Enter number of rental days: "))
print("Rental Charges: ₹", v.rental_charges(days))

v.return_vehicle()
v.display()
#11
class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = []

    def add_product(self, name, price):
        self.products.append([name, price])
        print(name, "added to cart.")

    def remove_product(self, name):
        for product in self.products:
            if product[0] == name:
                self.products.remove(product)
                print(name, "removed from cart.")
                return

        print("Product not found.")

    def total_bill(self):
        total = 0
        for product in self.products:
            total += product[1]

        return total

    def display(self):
        print("Customer Name:", self.customer_name)
        print("Cart ID:", self.cart_id)
        print("Products:")

        for product in self.products:
            print(product[0], "₹", product[1])

        print("Total Bill: ₹", self.total_bill())

    def __del__(self):
        print("Shopping cart object destroyed.")


cart = ShoppingCart("Priya", 101)

cart.add_product("Bag", 1000)
cart.add_product("Shoes", 2000)
cart.add_product("Watch", 1500)

cart.display()

cart.remove_product("Watch")

cart.display()

del cart
#12
class FoodOrder:
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def total_bill(self):
        subtotal = self.quantity * self.price
        tax = subtotal * 0.05
        total = subtotal + tax
        return total

    def display(self):
        print("Order ID:", self.order_id)
        print("Customer Name:", self.customer_name)
        print("Food Item:", self.food_item)
        print("Quantity:", self.quantity)
        print("Price per Item: ₹", self.price)
        print("Total Bill including 5% tax: ₹", self.total_bill())

    def __del__(self):
        print("Food order completed.")


order = FoodOrder(101, "Rahul", "Pizza", 2, 300)

order.display()

del order
#13
class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / 5

    def grade(self):
        percentage = self.percentage()

        if percentage >= 90:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        else:
            return "F"

    def display(self):
        print("Student Name:", self.name)
        print("Marks:", self.marks)
        print("Total:", self.total())
        print("Percentage:", self.percentage(), "%")
        print("Grade:", self.grade())

    def __del__(self):
        print("Student result object destroyed.")


student = StudentResult("Sneha", [85, 90, 78, 88, 92])

student.display()

del student
