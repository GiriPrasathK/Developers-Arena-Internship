# --------------------------------------------------
# Student Grade Calculator
# Author: Your Name
# Description: Calculates grades, comments, and
# statistics for multiple students
# --------------------------------------------------

def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"


def grade_comment(grade):
    comments = {
        "A": "Excellent performance 🌟",
        "B": "Very good work 👍",
        "C": "Good effort 🙂",
        "D": "Needs improvement ⚠️",
        "F": "Fail – work harder ❌"
    }
    return comments.get(grade, "")


def get_valid_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter marks for {subject} (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Enter a number.")


def main():
    students = []
    results = []

    while True:
        try:
            n = int(input("Enter number of students: "))
            if n > 0:
                break
            else:
                print("Number must be positive.")
        except ValueError:
            print("Invalid input.")

    for i in range(n):
        print(f"\nStudent {i + 1}")
        name = input("Enter student name: ")

        m1 = get_valid_marks("Subject 1")
        m2 = get_valid_marks("Subject 2")
        m3 = get_valid_marks("Subject 3")

        avg = round((m1 + m2 + m3) / 3, 2)
        grade = calculate_grade(avg)
        comment = grade_comment(grade)

        students.append(name)
        results.append([name, avg, grade, comment])

    averages = [r[1] for r in results]

    print("\n📊 STUDENT RESULTS")
    print("-" * 60)
    print(f"{'Name':<15}{'Average':<10}{'Grade':<10}Comment")
    print("-" * 60)

    for r in results:
        print(f"{r[0]:<15}{r[1]:<10}{r[2]:<10}{r[3]}")

    print("\n📈 CLASS STATISTICS")
    print(f"Class Average: {round(sum(averages)/len(averages), 2)}")
    print(f"Highest Average: {max(averages)}")
    print(f"Lowest Average: {min(averages)}")

    with open("results_sample.txt", "w") as file:
        for r in results:
            file.write(f"{r[0]}, {r[1]}, {r[2]}, {r[3]}\n")

    print("\nResults saved to results_sample.txt")


if __name__ == "__main__":
    main()
