# Student Performance & Access Management System

# 1. Login Validation

users = {
    "trainer1": "Train@123",
    "trainer2": "Learn@123"
}

attempts = 0
login_success = False

while attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username in users and users[username] == password:
        print("Login successful\n")
        login_success = True
        break
    else:
        attempts += 1
        print("Invalid credentials")

if not login_success:
    print("Access Denied. Please contact admin.")
    exit()

# 2. Trainee Data Entry

trainees = []

for i in range(3):  # min 3 trainee
    print("\nEnter details for Trainee", i + 1)
    name = input("Trainee Name: ")

    # Input marks with validation
    while True:
        python = float(input("Python Basics Marks: "))
        if 0 <= python <= 100:
            break
        print("Invalid marks. Enter between 0 and 100.")

    while True:
        ds = float(input("Data Structures Marks: "))
        if 0 <= ds <= 100:
            break
        print("Invalid marks. Enter between 0 and 100.")

    while True:
        cf = float(input("Control Flow Marks : "))
        if 0 <= cf <= 100:
            break
        print("Invalid marks. Enter between 0 and 100.\n")

    total = python + ds + cf
    average = total / 3

    # Grade calculation
    if average >= 85:
        grade = "Excellent"
    elif average >= 70:
        grade = "Good"
    elif average >= 50:
        grade = "Average"
    else:
        grade = "Needs Improvement"

    trainees.append([name, python, ds, cf, total, average, grade])

# 3. Performance Evaluation

print("Performance Report")

# Highest & Lowest Average (without max/min)
highest = trainees[0]
lowest = trainees[0]

for t in trainees:
    if t[5] > highest[5]:
        highest = t
    if t[5] < lowest[5]:
        lowest = t

print("Highest Average Scorer:", highest[0], "-", round(highest[5], 2))
print("Lowest Average Scorer:", lowest[0], "-", round(lowest[5], 2))

# Grade count
excellent = good = average_count = need_improve = 0

for t in trainees:
    if t[6] == "Excellent":
        excellent += 1
    elif t[6] == "Good":
        good += 1
    elif t[6] == "Average":
        average_count += 1
    else:
        need_improve += 1

print("\nGrade Distribution:")
print("Excellent:", excellent)
print("Good:", good)
print("Average:", average_count)
print("Needs Improvement:", need_improve)

# Failed any subject (<40)
print("Trainees who failed in any subject:")
failed = []

for t in trainees:
    if t[1] < 40 or t[2] < 40 or t[3] < 40:
        print(t[0])
        failed.append(t[0])

if len(failed) == 0:
    print("None")

# 5. Trainer Decision Module

choice = input("Do you want to schedule remedial training? (yes/no): ")

if choice.lower() == "yes":
    print("Trainees needing remedial training:")
    for t in trainees:
        if t[6] == "Needs Improvement" or t[0] in failed:
            print(t[0])
else:
    print("Report finalized successfully")