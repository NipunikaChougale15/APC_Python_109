"""
==============================================================
PYTHON DICTIONARY PROGRAMS  (Problems 1 - 35)
==============================================================
Each problem is written as its own function so you can run them
individually in VS Code (Right-click -> "Run Python File" or use
the "Run Cell" / interactive window, or simply call the function
you need from the bottom `if __name__ == "__main__":` block).

Programs that explicitly say "accept from the user" / "
"""


# ------------------------------------------------------------
# 1. Student details dictionary (roll no, name, dept, marks)
# ------------------------------------------------------------
def problem1():
    print("\n--- Problem 1: Student Details ---")
    student = {
        "roll_number": 101,
        "name": "Aarav Sharma",
        "department": "Computer Science",
        "marks": 88
    }
    for key, value in student.items():
        print(f"{key}: {value}")


# ------------------------------------------------------------
# 2. Employee info dictionary - display value for a given key
# ------------------------------------------------------------
def problem2():
    print("\n--- Problem 2: Employee Info ---")
    employee = {
        "emp_id": "E001",
        "name": "Priya Verma",
        "designation": "Software Engineer",
        "salary": 65000
    }
    key = "designation"          # specified key
    if key in employee:
        print(f"Value for key '{key}': {employee[key]}")
    else:
        print(f"Key '{key}' not found in dictionary.")


# ------------------------------------------------------------
# 3. Five products and prices - add a new product
# ------------------------------------------------------------
def problem3():
    print("\n--- Problem 3: Products and Prices ---")
    products = {
        "Laptop": 55000,
        "Mouse": 500,
        "Keyboard": 800,
        "Monitor": 9000,
        "Printer": 6500
    }
    print("Before adding:", products)
    products["Webcam"] = 1800      # add new product
    print("After adding:", products)


# ------------------------------------------------------------
# 4. Student marks dictionary - update marks of a student
# ------------------------------------------------------------
def problem4():
    print("\n--- Problem 4: Update Student Marks ---")
    marks = {"Amit": 78, "Neha": 85, "Rohit": 62, "Sneha": 91}
    print("Before update:", marks)
    student_to_update = "Rohit"
    new_marks = 75
    if student_to_update in marks:
        marks[student_to_update] = new_marks
    print("After update:", marks)


# ------------------------------------------------------------
# 5. Cities and populations - remove a specified city
# ------------------------------------------------------------
def problem5():
    print("\n--- Problem 5: Remove a City ---")
    population = {
        "Mumbai": 20411000,
        "Delhi": 16787941,
        "Bengaluru": 8443675,
        "Pune": 3124458,
        "Chennai": 7088000
    }
    print("Before removal:", population)
    city_to_remove = "Chennai"
    population.pop(city_to_remove, None)
    print("After removal:", population)


# ------------------------------------------------------------
# 6. Employee IDs and names - check if an entered ID exists
# ------------------------------------------------------------
def problem6():
    print("\n--- Problem 6: Check Employee ID ---")
    employees = {101: "Karan", 102: "Divya", 103: "Manoj"}
    emp_id = input("Enter employee ID to check: ")
    try:
        emp_id = int(emp_id)
    except ValueError:
        print("Invalid ID entered.")
        return
    if emp_id in employees:
        print(f"Employee ID {emp_id} exists. Name: {employees[emp_id]}")
    else:
        print(f"Employee ID {emp_id} does not exist.")


# ------------------------------------------------------------
# 7. Student records - total number of key-value pairs
# ------------------------------------------------------------
def problem7():
    print("\n--- Problem 7: Total Key-Value Pairs ---")
    records = {"Roll1": "Aman", "Roll2": "Bina", "Roll3": "Chetan", "Roll4": "Divya"}
    print("Dictionary:", records)
    print("Total key-value pairs:", len(records))


# ------------------------------------------------------------
# 8. Display all keys, all values, all key-value pairs
# ------------------------------------------------------------
def problem8():
    print("\n--- Problem 8: Keys, Values, Items ---")
    data = {"a": 1, "b": 2, "c": 3}
    print("All keys:", list(data.keys()))
    print("All values:", list(data.values()))
    print("All key-value pairs:", list(data.items()))


# ------------------------------------------------------------
# 9. Programming languages and creators - loop through them
# ------------------------------------------------------------
def problem9():
    print("\n--- Problem 9: Languages and Creators ---")
    languages = {
        "Python": "Guido van Rossum",
        "Java": "James Gosling",
        "C++": "Bjarne Stroustrup",
        "JavaScript": "Brendan Eich"
    }
    for language, creator in languages.items():
        print(f"{language} was created by {creator}")


# ------------------------------------------------------------
# 10. Accept 5 student names and marks from the user
# ------------------------------------------------------------
def problem10():
    print("\n--- Problem 10: Accept 5 Students and Marks ---")
    students = {}
    for i in range(5):
        name = input(f"Enter name of student {i + 1}: ")
        marks = float(input(f"Enter marks of {name}: "))
        students[name] = marks
    print("Student marks dictionary:", students)


# ------------------------------------------------------------
# 11. Student names and marks - find highest scorer
# ------------------------------------------------------------
def problem11():
    print("\n--- Problem 11: Highest Scorer ---")
    marks = {"Aman": 78, "Bina": 92, "Chetan": 85, "Divya": 67}
    topper = max(marks, key=marks.get)
    print(f"Student with highest marks: {topper} ({marks[topper]})")


# ------------------------------------------------------------
# 12. Student names and marks - find lowest scorer
# ------------------------------------------------------------
def problem12():
    print("\n--- Problem 12: Lowest Scorer ---")
    marks = {"Aman": 78, "Bina": 92, "Chetan": 85, "Divya": 67}
    lowest = min(marks, key=marks.get)
    print(f"Student with lowest marks: {lowest} ({marks[lowest]})")


# ------------------------------------------------------------
# 13. Student names and marks - calculate average marks
# ------------------------------------------------------------
def problem13():
    print("\n--- Problem 13: Average Marks ---")
    marks = {"Aman": 78, "Bina": 92, "Chetan": 85, "Divya": 67}
    average = sum(marks.values()) / len(marks)
    print(f"Average marks of all students: {average:.2f}")


# ------------------------------------------------------------
# 14. Accept a string - dictionary of character frequency
# ------------------------------------------------------------
def problem14():
    print("\n--- Problem 14: Character Frequency ---")
    text = input("Enter a string: ")
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    print("Character frequency dictionary:", freq)


# ------------------------------------------------------------
# 15. Accept a sentence - dictionary of word frequency
# ------------------------------------------------------------
def problem15():
    print("\n--- Problem 15: Word Frequency ---")
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    print("Word frequency dictionary:", freq)


# ------------------------------------------------------------
# 16. Merge two dictionaries into one
# ------------------------------------------------------------
def problem16():
    print("\n--- Problem 16: Merge Two Dictionaries ---")
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    merged = {**dict1, **dict2}
    print("Dictionary 1:", dict1)
    print("Dictionary 2:", dict2)
    print("Merged dictionary:", merged)


# ------------------------------------------------------------
# 17. Two dictionaries - find common keys
# ------------------------------------------------------------
def problem17():
    print("\n--- Problem 17: Common Keys ---")
    dict1 = {"a": 1, "b": 2, "c": 3}
    dict2 = {"b": 20, "c": 30, "d": 40}
    common_keys = dict1.keys() & dict2.keys()
    print("Common keys:", common_keys)


# ------------------------------------------------------------
# 18. Two dictionaries - find common values
# ------------------------------------------------------------
def problem18():
    print("\n--- Problem 18: Common Values ---")
    dict1 = {"a": 1, "b": 2, "c": 3}
    dict2 = {"x": 2, "y": 3, "z": 4}
    common_values = set(dict1.values()) & set(dict2.values())
    print("Common values:", common_values)


# ------------------------------------------------------------
# 19. Dictionary with duplicate values - remove duplicates
# ------------------------------------------------------------
def problem19():
    print("\n--- Problem 19: Remove Duplicate Values ---")
    data = {"a": 10, "b": 20, "c": 10, "d": 30, "e": 20}
    print("Original dictionary:", data)
    unique_values = {}
    result = {}
    for key, value in data.items():
        if value not in unique_values:
            unique_values[value] = key
            result[key] = value
    print("Dictionary after removing duplicate values:", result)


# ------------------------------------------------------------
# 20. Display dictionary elements in ascending order of keys
# ------------------------------------------------------------
def problem20():
    print("\n--- Problem 20: Sort by Keys (Ascending) ---")
    data = {"banana": 3, "apple": 5, "cherry": 2, "date": 8}
    sorted_dict = dict(sorted(data.items()))
    print("Original dictionary:", data)
    print("Sorted by keys:", sorted_dict)


# ------------------------------------------------------------
# 21. Numbers 1-10 as keys, squares as values
# ------------------------------------------------------------
def problem21():
    print("\n--- Problem 21: Squares (1 to 10) ---")
    squares = {num: num ** 2 for num in range(1, 11)}
    print(squares)


# ------------------------------------------------------------
# 22. Numbers 1-20 as keys, squares as values, only even numbers
# ------------------------------------------------------------
def problem22():
    print("\n--- Problem 22: Squares of Even Numbers (1 to 20) ---")
    squares = {num: num ** 2 for num in range(1, 21) if num % 2 == 0}
    print(squares)


# ------------------------------------------------------------
# 23. List of numbers - dictionary of unique numbers & frequency
# ------------------------------------------------------------
def problem23():
    print("\n--- Problem 23: Number Frequency from a List ---")
    numbers = [1, 2, 2, 3, 4, 4, 4, 5, 1, 6]
    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
    print("List:", numbers)
    print("Frequency dictionary:", freq)


# ------------------------------------------------------------
# 24. Integers 1-10 and their cubes
# ------------------------------------------------------------
def problem24():
    print("\n--- Problem 24: Cubes (1 to 10) ---")
    cubes = {num: num ** 3 for num in range(1, 11)}
    print(cubes)


# ------------------------------------------------------------
# 25. Student management system (add, update, delete, search,
#     display, highest marks, average)
# ------------------------------------------------------------
class StudentManager:
    def __init__(self):
        self.students = {"Aman": 78, "Bina": 92, "Chetan": 85}

    def add_student(self, name, marks):
        self.students[name] = marks

    def update_marks(self, name, marks):
        if name in self.students:
            self.students[name] = marks
        else:
            print(f"{name} not found.")

    def delete_student(self, name):
        self.students.pop(name, None)

    def search_student(self, name):
        return self.students.get(name, "Not found")

    def display_all(self):
        for name, marks in self.students.items():
            print(f"{name}: {marks}")

    def highest_marks(self):
        topper = max(self.students, key=self.students.get)
        return topper, self.students[topper]

    def average_marks(self):
        return sum(self.students.values()) / len(self.students)


def problem25():
    print("\n--- Problem 25: Student Management System ---")
    manager = StudentManager()

    print("Initial students:")
    manager.display_all()

    manager.add_student("Divya", 67)
    print("\nAfter adding Divya:")
    manager.display_all()

    manager.update_marks("Chetan", 90)
    print("\nAfter updating Chetan's marks:")
    manager.display_all()

    manager.delete_student("Aman")
    print("\nAfter deleting Aman:")
    manager.display_all()

    print("\nSearching for Bina:", manager.search_student("Bina"))

    topper, marks = manager.highest_marks()
    print(f"\nHighest marks: {topper} ({marks})")

    print(f"Average marks: {manager.average_marks():.2f}")


# ------------------------------------------------------------
# 26. Employee names and salaries - highest, lowest, average,
#     employees earning more than 50,000
# ------------------------------------------------------------
def problem26():
    print("\n--- Problem 26: Employee Salaries ---")
    salaries = {
        "Karan": 45000,
        "Divya": 62000,
        "Manoj": 78000,
        "Sneha": 39000,
        "Rohit": 55000
    }
    highest_emp = max(salaries, key=salaries.get)
    lowest_emp = min(salaries, key=salaries.get)
    average_salary = sum(salaries.values()) / len(salaries)
    above_50k = {name: sal for name, sal in salaries.items() if sal > 50000}

    print("Salaries:", salaries)
    print(f"Highest salary: {highest_emp} ({salaries[highest_emp]})")
    print(f"Lowest salary: {lowest_emp} ({salaries[lowest_emp]})")
    print(f"Average salary: {average_salary:.2f}")
    print("Employees earning more than 50,000:", above_50k)


# ------------------------------------------------------------
# 27. Product names and quantities - add, update, delete,
#     search, display products with quantity below 10
# ------------------------------------------------------------
class ProductManager:
    def __init__(self):
        self.products = {"Rice": 50, "Sugar": 8, "Salt": 20, "Oil": 5, "Wheat": 40}

    def add_product(self, name, qty):
        self.products[name] = qty

    def update_quantity(self, name, qty):
        if name in self.products:
            self.products[name] = qty
        else:
            print(f"{name} not found.")

    def delete_product(self, name):
        self.products.pop(name, None)

    def search_product(self, name):
        return self.products.get(name, "Not found")

    def low_stock(self, threshold=10):
        return {name: qty for name, qty in self.products.items() if qty < threshold}


def problem27():
    print("\n--- Problem 27: Product Inventory ---")
    manager = ProductManager()
    print("Initial products:", manager.products)

    manager.add_product("Tea", 15)
    print("\nAfter adding Tea:", manager.products)

    manager.update_quantity("Salt", 3)
    print("\nAfter updating Salt quantity:", manager.products)

    manager.delete_product("Wheat")
    print("\nAfter deleting Wheat:", manager.products)

    print("\nSearch 'Rice':", manager.search_product("Rice"))

    print("\nProducts with quantity below 10:", manager.low_stock())


# ------------------------------------------------------------
# 28. Names and phone numbers - add, search, update, delete,
#     display all contacts
# ------------------------------------------------------------
class ContactManager:
    def __init__(self):
        self.contacts = {"Aman": "9876543210", "Bina": "9123456780"}

    def add_contact(self, name, number):
        self.contacts[name] = number

    def search_contact(self, name):
        return self.contacts.get(name, "Not found")

    def update_contact(self, name, number):
        if name in self.contacts:
            self.contacts[name] = number
        else:
            print(f"{name} not found.")

    def delete_contact(self, name):
        self.contacts.pop(name, None)

    def display_all(self):
        for name, number in self.contacts.items():
            print(f"{name}: {number}")


def problem28():
    print("\n--- Problem 28: Contact Book ---")
    manager = ContactManager()

    manager.add_contact("Chetan", "9988776655")
    print("After adding Chetan:")
    manager.display_all()

    print("\nSearch 'Aman':", manager.search_contact("Aman"))

    manager.update_contact("Bina", "9111122223")
    print("\nAfter updating Bina's number:")
    manager.display_all()

    manager.delete_contact("Aman")
    print("\nAfter deleting Aman:")
    manager.display_all()


# ------------------------------------------------------------
# 29. Book IDs and book names - add, search, remove, display,
#     count total books
# ------------------------------------------------------------
class BookManager:
    def __init__(self):
        self.books = {"B001": "The Alchemist", "B002": "Python Basics"}

    def add_book(self, book_id, name):
        self.books[book_id] = name

    def search_book(self, book_id):
        return self.books.get(book_id, "Not found")

    def remove_book(self, book_id):
        self.books.pop(book_id, None)

    def display_all(self):
        for book_id, name in self.books.items():
            print(f"{book_id}: {name}")

    def total_books(self):
        return len(self.books)


def problem29():
    print("\n--- Problem 29: Book Catalog ---")
    manager = BookManager()

    manager.add_book("B003", "Data Structures in Python")
    print("After adding B003:")
    manager.display_all()

    print("\nSearch 'B002':", manager.search_book("B002"))

    manager.remove_book("B001")
    print("\nAfter removing B001:")
    manager.display_all()

    print("\nTotal books:", manager.total_books())


# ------------------------------------------------------------
# 30. Group students by department
# ------------------------------------------------------------
def problem30():
    print("\n--- Problem 30: Group Students by Department ---")
    students = {
        "Aman": "CSE",
        "Bina": "ECE",
        "Chetan": "CSE",
        "Divya": "Mech",
        "Esha": "ECE"
    }
    grouped = {}
    for name, dept in students.items():
        grouped.setdefault(dept, []).append(name)
    print("Original dictionary:", students)
    print("Grouped by department:", grouped)


# ------------------------------------------------------------
# 31. List of words - dictionary of word length -> list of words
# ------------------------------------------------------------
def problem31():
    print("\n--- Problem 31: Group Words by Length ---")
    words = ["cat", "dog", "apple", "ant", "banana", "fig", "kiwi"]
    grouped = {}
    for word in words:
        grouped.setdefault(len(word), []).append(word)
    print("Words:", words)
    print("Grouped by length:", grouped)


# ------------------------------------------------------------
# 32. List of integers and a target - find two numbers whose
#     sum equals the target (using a dictionary)
# ------------------------------------------------------------
def problem32():
    print("\n--- Problem 32: Two Sum Using Dictionary ---")
    numbers = [2, 7, 11, 15, 3, 6]
    target = 9
    seen = {}
    result = None
    for num in numbers:
        complement = target - num
        if complement in seen:
            result = (complement, num)
            break
        seen[num] = True
    print("List:", numbers, "| Target:", target)
    print("Pair found:", result if result else "No pair found")


# ------------------------------------------------------------
# 33. String - first character that occurs only once
# ------------------------------------------------------------
def problem33():
    print("\n--- Problem 33: First Non-Repeating Character ---")
    text = "swiss"
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    result = next((ch for ch in text if freq[ch] == 1), None)
    print(f"String: '{text}'")
    print("First non-repeating character:", result if result else "None found")


# ------------------------------------------------------------
# 34. String - first character that occurs more than once
# ------------------------------------------------------------
def problem34():
    print("\n--- Problem 34: First Repeating Character ---")
    text = "swiss"
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    result = next((ch for ch in text if freq[ch] > 1), None)
    print(f"String: '{text}'")
    print("First repeating character:", result if result else "None found")


# ------------------------------------------------------------
# 35. Paragraph - dictionary of word length -> number of words
#     having that length
# ------------------------------------------------------------
def problem35():
    print("\n--- Problem 35: Word Count by Length ---")
    paragraph = "Python is a simple yet powerful programming language"
    words = paragraph.split()
    freq = {}
    for word in words:
        length = len(word)
        freq[length] = freq.get(length, 0) + 1
    print("Paragraph:", paragraph)
    print("Word-length frequency dictionary:", freq)


# ==============================================================
# MAIN — runs every problem in sequence
# (Problems 6, 10, 14, 15 will ask you for input)
# ==============================================================
if __name__ == "__main__":
    all_problems = [
        problem1, problem2, problem3, problem4, problem5,
        problem6, problem7, problem8, problem9, problem10,
        problem11, problem12, problem13, problem14, problem15,
        problem16, problem17, problem18, problem19, problem20,
        problem21, problem22, problem23, problem24, problem25,
        problem26, problem27, problem28, problem29, problem30,
        problem31, problem32, problem33, problem34, problem35,
    ]

    for func in all_problems:
        func()