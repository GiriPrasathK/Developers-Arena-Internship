# Name: Giriprasath K
# Project: Student Grade Calculator
# Description:
# A Python program that collects student marks, calculates averages,
# assigns grades with comments, stores results using lists,
# displays statistics, and saves data to a file.

# -------------------------------
# Grade & Comment Functions
# -------------------------------

def calculate_grade(avg):
    if 90 <= avg <= 100:
        return "A"
    elif 80 <= avg < 90:
        return "B"
    elif 70 <= avg < 80:
        return "C"
    elif 60 <= avg < 70:
        return "D"
    else:
        return "F"


def grade_comment(grade):
    if grade == "A":
        return "Excellent performance!"
    elif grade == "B":
        return "Very good work."
    elif grade == "C":
        return "Good, but can improve."
    elif grade == "D":
        return "Needs more effort."
    else:
        return "Poor performance. Needs serious improvement."


# -------------------------------
# Input Validation Helpers
# -------------------------------

def get_valid_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("❌ Enter a positive number.")
        except ValueError:
            print("❌ Invalid input. Enter a number.")


def get_valid_mark(subject):
    while True:
        try:
            mark = float(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= mark <= 100:
                return mark
            else:
                print("❌ Marks must be between 0 and 100.")
        except ValueError:
            print("❌ Invalid input. Enter numeric marks.")


# -------------------------------
# Main Program
# -------------------------------

print("=" * 60)
print("WELCOME TO STUDENT GRADE CALCULATOR")
print("=" * 60)

num_students = get_valid_number("Enter number of students: ")

students = []
results = []

# -------------------------------
# Collect Student Data
# -------------------------------

for i in range(num_students):
    print(f"\n--- Student {i + 1} ---")
    name = input("Enter student name: ").strip().title()

    marks = []
    for subject in ["Subject 1", "Subject 2", "Subject 3"]:
        marks.append(get_valid_mark(subject))

    average = sum(marks) / len(marks)
    grade = calculate_grade(average)
    comment = grade_comment(grade)

    students.append(name)
    results.append([name, marks, average, grade, comment])

# -------------------------------
# Class Statistics
# -------------------------------

averages = [student[2] for student in results]
class_avg = sum(averages) / len(averages)
highest = max(averages)
lowest = min(averages)

# -------------------------------
# Display Results Table
# -------------------------------

print("\n" + "=" * 90)
print(f"{'Name':<15}{'Marks':<25}{'Average':<10}{'Grade':<8}Comment")
print("=" * 90)

for r in results:
    print(f"{r[0]:<15}{str(r[1]):<25}{r[2]:<10.2f}{r[3]:<8}{r[4]}")

print("=" * 90)
print(f"Class Average : {class_avg:.2f}")
print(f"Highest Avg   : {highest:.2f}")
print(f"Lowest Avg    : {lowest:.2f}")
print("=" * 90)

# -------------------------------
# Search Feature
# -------------------------------

search = input("\nSearch for a student by name (or press Enter to skip): ").strip().title()
if search:
    found = False
    for r in results:
        if r[0] == search:
            print(f"\nResult for {search}: Avg={r[2]:.2f}, Grade={r[3]}, Comment={r[4]}")
            found = True
            break
    if not found:
        print("❌ Student not found.")

# -------------------------------
# Save Results to File
# -------------------------------

with open("results.txt", "w") as file:
    for r in results:
        file.write(f"{r[0]}, {r[1]}, {r[2]:.2f}, {r[3]}, {r[4]}\n")

print("\n✅ Results saved to results.txt")
print("Thank you for using the Grade Calculator!")
