# 1. Student Class
class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks  # dictionary of subject: marks

    def display(self):
        total = sum(self.marks.values())
        percentage = total / (len(self.marks) * 100) * 100
        print(f"Roll No: {self.roll_no}, Name: {self.name}, Percentage: {percentage:.2f}%")

# 2. Employee Class
class Employee:
    def __init__(self, emp_id, name, basic_salary):
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary(self):
        hra = 0.2 * self.basic_salary
        da = 0.1 * self.basic_salary
        gross = self.basic_salary + hra + da
        print(f"Emp ID: {self.emp_id}, Name: {self.name}, Gross Salary: {gross}")

# 3. Rectangle Class
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

# 4. Circle Class
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14159 * self.radius

# 5. Book Class
class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Price: {self.price}")

# 6. ElectricityBill Class
class ElectricityBill:
    def __init__(self, consumer_no, consumer_name, units):
        self.consumer_no = consumer_no
        self.consumer_name = consumer_name
        self.units = units

    def calculate_bill(self):
        if self.units <= 100:
            bill = self.units * 5
        elif self.units <= 200:
            bill = (100 * 5) + (self.units - 100) * 7
        else:
            bill = (100 * 5) + (100 * 7) + (self.units - 200) * 10
        print(f"Consumer: {self.consumer_name}, Bill: {bill}")

# 7. MobilePhone Class
class MobilePhone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.price = price

    def display_specs(self):
        print(f"{self.brand} {self.model}, Storage: {self.storage}, Price: {self.price}")

    def discounted_price(self, discount):
        return self.price - (self.price * discount / 100)

# 8. Patient Class
class Patient:
    def __init__(self, patient_id, name, age, disease, fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.fee = fee

    def display(self):
        print(f"Patient ID: {self.patient_id}, Name: {self.name}, Age: {self.age}, Disease: {self.disease}, Fee: {self.fee}")

# 9. ATM Class
class ATM:
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def check_balance(self):
        print(f"Balance: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}, New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn {amount}, New Balance: {self.balance}")
        else:
            print("Insufficient Balance")

    def display_details(self):
        print(f"Account No: {self.acc_no}, Name: {self.name}, Balance: {self.balance}")

# 10. Vehicle Class
class Vehicle:
    def __init__(self, number, model, rate, available=True):
        self.number = number
        self.model = model
        self.rate = rate
        self.available = available

    def rent(self, days):
        if self.available:
            self.available = False
            print(f"Vehicle rented for {days} days. Charge: {self.rate * days}")
        else:
            print("Vehicle not available")

    def return_vehicle(self):
        self.available = True
        print("Vehicle returned")

# 11. ShoppingCart Class
class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = {}

    def add_product(self, name, price):
        self.products[name] = price

    def remove_product(self, name):
        if name in self.products:
            del self.products[name]

    def total_bill(self):
        return sum(self.products.values())

    def __del__(self):
        print("Shopping cart destroyed")

# 12. FoodOrder Class
class FoodOrder:
    def __init__(self, order_id, customer_name, item, qty, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.item = item
        self.qty = qty
        self.price = price

    def total_bill(self):
        return self.qty * self.price * 1.05  # 5% tax

    def __del__(self):
        print("Order completed")

# 13. StudentResult Class
class StudentResult:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def total(self):
        return sum(self.marks)

    def percentage(self):
        return self.total() / (len(self.marks) * 100) * 100

    def grade(self):
        p = self.percentage()
        if p >= 75:
            return "A"
        elif p >= 50:
            return "B"
        else:
            return "C"

    def __del__(self):
        print("Result object destroyed")


# ---------------- SAMPLE USAGE ----------------
if __name__ == "__main__":
    s1 = Student(1, "Alice", {"Math": 90, "Science": 80, "English": 85})
    s1.display()

    e1 = Employee(101, "Bob", 30000)
    e1.calculate_salary()

    r = Rectangle(10, 5)
    print("Rectangle Area:", r.area(), "Perimeter:", r.perimeter())

    c = Circle(7)
    print("Circle Area:", c.area(), "Circumference:", c.circumference())

    b1 = Book(1, "Python Basics", "John Doe", 500)
    b1.display()

    bill = ElectricityBill(123, "Charlie", 250)
    bill.calculate_bill()

    phone = MobilePhone("Samsung", "Galaxy S21", "128GB", 70000)
    phone.display_specs()
    print("Discounted Price:", phone.discounted_price(10))

    p1 = Patient(1, "David", 45, "Flu", 500)
    p1.display()

    atm = ATM(1001, "Eve", 1000)
    atm.check_balance()
    atm.deposit(500)
    atm.withdraw(300)
    atm.display_details()

    v = Vehicle("MH12AB1234", "Honda City", 1000)
    v.rent(3)
    v.return_vehicle()

    cart = ShoppingCart("Frank", 2001)
    cart.add_product("Laptop", 50000)
    cart.add_product("Mouse", 500)
    print("Total Bill:", cart.total_bill())
    del cart

    order = FoodOrder(3001, "Grace", "Pizza", 2, 250)
    print("Total Bill:", order.total_bill())
    del order

    result = StudentResult("Helen", [80, 70, 90, 85, 75])
    print("Total:", result.total(), "Percentage:", result.percentage(), "Grade:", result.grade())
    del result
