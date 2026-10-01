import pandas as pd


# Students CSV
students_csv = {
    "Student_ID":[1,2,3,4,5],
    "Name":["Amit","Priya","Ravi","Sneha","Karan"],
    "Department":["CSE","IT","CSE","IT","CSE"],
    "Python":[80,70,90,60,85],
    "DBMS":[75,65,95,55,80],
    "Maths":[70,60,85,50,90]
}
pd.DataFrame(students_csv).to_csv("students.csv", index=False)

# Employees CSV
employees_csv = {
    "Employee_ID":[101,102,103,104],
    "Name":["Raj","Meena","Arun","Neha"],
    "Department":["CSE","IT","HR","Finance"],
    "Experience":[5,3,10,7],
    "Salary":[60000,45000,70000,55000]
}
pd.DataFrame(employees_csv).to_csv("employees.csv", index=False)

# Patients CSV
patients_csv = {
    "Patient_ID":[201,202,203,204],
    "Name":["A","B","C","D"],
    "Age":[65,45,70,30],
    "Gender":["M","F","M","F"],
    "Disease":["Flu","Cancer","Diabetes","Asthma"],
    "Medical_Expense":[60000,40000,80000,30000]
}
pd.DataFrame(patients_csv).to_csv("patients.csv", index=False)

# Weather CSV
weather_csv = {
    "Date":["2026-10-01"]*5,
    "City":["Mumbai","Delhi","Pune","Chennai","Bangalore"],
    "Temperature":[36,32,28,38,30],
    "Humidity":[70,60,65,75,68],
    "Rainfall":[12,5,8,20,10]
}
pd.DataFrame(weather_csv).to_csv("weather.csv", index=False)

print("CSV files generated successfully!\n")

# ------------------ 1. Student Marks ------------------
students = {
    "Student_ID": [1, 2, 3, 4, 5],
    "Name": ["Amit", "Priya", "Ravi", "Sneha", "Karan"],
    "Python": [80, 70, 90, 60, 85],
    "DBMS": [75, 65, 95, 55, 80],
    "Maths": [70, 60, 85, 50, 90]
}
df_students = pd.DataFrame(students)
df_students["Total"] = df_students[["Python","DBMS","Maths"]].sum(axis=1)
df_students["Average"] = df_students["Total"]/3
print("\nStudents DataFrame:\n", df_students)
print("\nStudents with >75% average:\n", df_students[df_students["Average"]>75])

# ------------------ 2. Employee Data ------------------
employees = {
    "Emp_ID":[101,102,103,104],
    "Name":["Raj","Meena","Arun","Neha"],
    "Dept":["CSE","IT","HR","Finance"],
    "Salary":[60000,45000,70000,55000],
    "Experience":[5,3,10,7]
}
df_emp = pd.DataFrame(employees)
print("\nEmployees with salary >50000:\n", df_emp[df_emp["Salary"]>50000])
print("\nAverage Salary:", df_emp["Salary"].mean())
print("Highest Salary:", df_emp["Salary"].max())
print("Employee with highest experience:\n", df_emp.loc[df_emp["Experience"].idxmax()])

# ------------------ 3. Product Sales ------------------
products = {
    "Prod_ID":[1,2,3],
    "Name":["Laptop","Mobile","Tablet"],
    "Category":["Electronics","Electronics","Electronics"],
    "Price":[50000,20000,15000],
    "Quantity":[10,30,20]
}
df_prod = pd.DataFrame(products)
df_prod["Total_Sales"] = df_prod["Price"]*df_prod["Quantity"]
print("\nProduct with highest sales:\n", df_prod.loc[df_prod["Total_Sales"].idxmax()])

# ------------------ 4. Patient Data ------------------
patients = {
    "Patient_ID":[1,2,3,4],
    "Name":["A","B","C","D"],
    "Age":[65,45,70,30],
    "Disease":["Flu","Cancer","Diabetes","Asthma"],
    "Charges":[60000,40000,80000,30000]
}
df_pat = pd.DataFrame(patients)
print("\nPatients above 60:\n", df_pat[df_pat["Age"]>60])
print("Average Charges:", df_pat["Charges"].mean())
print("Max Charges:", df_pat["Charges"].max())
print("Patients with charges >50000:\n", df_pat[df_pat["Charges"]>50000])

# ------------------ 5. Orders ------------------
orders = {
    "Order_ID":[1,2,3],
    "Customer":["X","Y","Z"],
    "Product":["Laptop","Mobile","Tablet"],
    "Quantity":[1,2,3],
    "Price":[50000,20000,15000],
    "Discount":[2000,1000,500]
}
df_orders = pd.DataFrame(orders)
df_orders["Final_Amount"] = df_orders["Quantity"]*df_orders["Price"]-df_orders["Discount"]
print("\nAll Orders:\n", df_orders)
print("\nOrders above 5000:\n", df_orders[df_orders["Final_Amount"]>5000])
print("Highest Order:\n", df_orders.loc[df_orders["Final_Amount"].idxmax()])
print("Average Order Value:", df_orders["Final_Amount"].mean())

# ------------------ 6. Attendance ------------------
attendance = {
    "Student_ID":[1,2,3],
    "Name":["Amit","Priya","Ravi"],
    "Dept":["CSE","IT","CSE"],
    "Total_Classes":[100,100,100],
    "Attended":[70,90,60]
}
df_att = pd.DataFrame(attendance)
df_att["Attendance%"] = (df_att["Attended"]/df_att["Total_Classes"])*100
print("\nStudents below 75% attendance:\n", df_att[df_att["Attendance%"]<75])

# ------------------ 7. Retail Shop ------------------
shop = {
    "Prod_ID":[1,2,3],
    "Name":["Shirt","Jeans","Shoes"],
    "Category":["Clothes","Clothes","Footwear"],
    "Price":[1000,2000,3000],
    "Quantity":[20,15,10]
}
df_shop = pd.DataFrame(shop)
df_shop["Total_Sales"] = df_shop["Price"]*df_shop["Quantity"]
print("\nProducts with sales >10000:\n", df_shop[df_shop["Total_Sales"]>10000])
print("Product with max sales:\n", df_shop.loc[df_shop["Total_Sales"].idxmax()])
print("Average Sales:", df_shop["Total_Sales"].mean())

# ------------------ 8. Student Marks Series ------------------
marks = {"Amit":80,"Priya":70,"Ravi":90,"Sneha":60}
s_marks = pd.Series(marks)
print("\nMarks Series:\n", s_marks)
print("Marks of Ravi:", s_marks["Ravi"])
print("Max:", s_marks.max(),"Min:", s_marks.min())
print("Average:", s_marks.mean())
print("Students >75:\n", s_marks[s_marks>75])

# ------------------ 9. Employee Salary Series ------------------
salary = {"Raj":60000,"Meena":45000,"Arun":70000,"Neha":55000}
s_sal = pd.Series(salary)
print("\nHighest Salary:", s_sal.max())
print("Lowest Salary:", s_sal.min())
print("Average Salary:", s_sal.mean())
print("Employees >50000:\n", s_sal[s_sal>50000])

# ------------------ 10. Product Price Series ------------------
prices = {"Laptop":50000,"Mobile":20000,"Tablet":15000}
s_price = pd.Series(prices)
print("\nPrices +10%:\n", s_price*1.1)
print("Most Expensive:", s_price.idxmax())
print("Products >1000:\n", s_price[s_price>1000])

# ------------------ 11. Patient Age Series ------------------
ages = {101:65,102:45,103:70,104:30}
s_age = pd.Series(ages)
print("\nAverage Age:", s_age.mean())
print("Oldest:", s_age.max(),"Youngest:", s_age.min())
print("Patients >60:\n", s_age[s_age>60])

# ------------------ 12. Attendance Series ------------------
att_series = {"Amit":70,"Priya":95,"Ravi":60}
s_att = pd.Series(att_series)
print("\nAverage Attendance:", s_att.mean())
print("Below 75:\n", s_att[s_att<75])
print("Above 90:\n", s_att[s_att>90])