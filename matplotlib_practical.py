import matplotlib.pyplot as plt

# 1. Line Plot
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
plt.plot(x, y, marker='o', color='blue')
plt.title("Line Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# 2. Bar Chart
subjects = ["Math", "Science", "English", "History"]
marks = [85, 90, 75, 80]
plt.bar(subjects, marks, color='green')
plt.title("Bar Chart Example")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()

# 3. Histogram
data = [12, 15, 17, 20, 21, 22, 23, 24, 25, 30, 35, 40, 45, 50]
plt.hist(data, bins=5, color='orange', edgecolor='black')
plt.title("Histogram Example")
plt.xlabel("Value Range")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter Plot
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]
plt.scatter(x, y, color='red')
plt.title("Scatter Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# 5. Pie Chart
activities = ["Study", "Sleep", "Play", "Eat"]
hours = [8, 7, 5, 4]
colors = ["gold", "lightblue", "lightgreen", "pink"]
plt.pie(hours, labels=activities, colors=colors, autopct='%1.1f%%')
plt.title("Pie Chart Example")
plt.show()
