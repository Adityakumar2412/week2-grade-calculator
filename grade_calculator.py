# grade_calculator.py
# Author: Aditya Kumar
# Week 2 Project - Student Grade Calculator (The Developers Arena)

def calculate_grade(average):
    """Return (grade, comment) based on average marks"""
    if average >= 90:
        return 'A', 'Excellent! Keep up the great work!'
    elif average >= 80:
        return 'B', "Very Good! You're doing well."
    elif average >= 70:
        return 'C', 'Good. Room for improvement.'
    elif average >= 60:
        return 'D', 'Needs Improvement. Please study more.'
    else:
        return 'F', 'Failed. Please seek help from teacher.'


def get_valid_number(prompt, min_val=0, max_val=100):
    """Get a valid number within specified range"""
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}")
        except ValueError:
            print("Invalid input! Please enter a number.")


def get_positive_int(prompt):
    """Get a valid positive integer"""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number!")
        except ValueError:
            print("Invalid input! Please enter a whole number.")


def input_students():
    """Collect student data and return structure with all results"""
    print("=" * 50)
    print("      STUDENT GRADE CALCULATOR")
    print("=" * 50)
    print()

    num_students = get_positive_int("Enter number of students: ")

    student_names = []
    student_marks = []   # list of [math, science, english]
    student_results = [] # list of dicts

    for i in range(num_students):
        print(f"\n=== STUDENT {i+1} ===")

        # name input
        name = input("Student name: ").strip()
        while name == "":
            print("Name cannot be empty!")
            name = input("Student name: ").strip()
        student_names.append(name)

        # marks input
        print("Enter marks (0-100):")
        math = get_valid_number("Math: ")
        science = get_valid_number("Science: ")
        english = get_valid_number("English: ")

        student_marks.append([math, science, english])

        # average, grade, comment
        average = (math + science + english) / 3
        grade, comment = calculate_grade(average)

        student_results.append({
            "average": average,
            "grade": grade,
            "comment": comment
        })

    return student_names, student_marks, student_results


def print_results(student_names, student_results):
    """Display formatted table of all students"""
    print("\n" + "=" * 50)
    print("            RESULTS SUMMARY")
    print("=" * 50)
    print(f"{'Name':<20} | {'Avg':>5} | {'Grade':^5} | Comment")
    print("-" * 60)

    for i, name in enumerate(student_names):
        avg = student_results[i]["average"]
        grade = student_results[i]["grade"]
        comment = student_results[i]["comment"]
        print(f"{name:<20} | {avg:>5.1f} | {grade:^5} | {comment}")


def class_statistics(student_names, student_results):
    """Calculate and print class stats (avg, max, min)"""
    if not student_results:
        print("No student data available!")
        return

    averages = [r["average"] for r in student_results]
    class_avg = sum(averages) / len(averages)
    max_avg = max(averages)
    min_avg = min(averages)
    max_index = averages.index(max_avg)
    min_index = averages.index(min_avg)

    print("\n" + "=" * 50)
    print("          CLASS STATISTICS")
    print("=" * 50)
    print(f"Total Students: {len(student_names)}")
    print(f"Class Average: {class_avg:.1f}")
    print(f"Highest Average: {max_avg:.1f} ({student_names[max_index]})")
    print(f"Lowest Average: {min_avg:.1f} ({student_names[min_index]})")


def search_student(student_names, student_results):
    """Search student by name and show details"""
    if not student_names:
        print("No student data to search!")
        return

    query = input("Enter student name to search: ").strip().lower()
    found = False

    for i, name in enumerate(student_names):
        if name.lower() == query:
            found = True
            avg = student_results[i]["average"]
            grade = student_results[i]["grade"]
            comment = student_results[i]["comment"]
            print("\nStudent found:")
            print("-" * 40)
            print(f"Name: {name}")
            print(f"Average: {avg:.1f}")
            print(f"Grade: {grade}")
            print(f"Comment: {comment}")
            print("-" * 40)
            break

    if not found:
        print("Student not found!")


def save_results_to_file(student_names, student_results, filename="results_output.txt"):
    """Save all results to a text file"""
    if not student_names:
        print("No data to save!")
        return

    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("STUDENT GRADE REPORT\n")
            f.write("=" * 50 + "\n")
            for i, name in enumerate(student_names):
                avg = student_results[i]["average"]
                grade = student_results[i]["grade"]
                comment = student_results[i]["comment"]
                f.write(f"Name   : {name}\n")
                f.write(f"Average: {avg:.1f}\n")
                f.write(f"Grade  : {grade}\n")
                f.write(f"Comment: {comment}\n")
                f.write("-" * 50 + "\n")
        print(f"Results saved to {filename}")
    except Exception as e:
        print("Error while saving file:", e)


def main_menu():
    """Menu system to handle operations"""
    student_names = []
    student_results = []

    while True:
        print("\n" + "=" * 50)
        print("            MAIN MENU")
        print("=" * 50)
        print("1. Enter student data and calculate grades")
        print("2. Show all results")
        print("3. Show class statistics")
        print("4. Search for a student")
        print("5. Save results to file")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            student_names, _, student_results = input_students()
        elif choice == "2":
            print_results(student_names, student_results)
        elif choice == "3":
            class_statistics(student_names, student_results)
        elif choice == "4":
            search_student(student_names, student_results)
        elif choice == "5":
            filename = input("Enter filename (default: results_output.txt): ").strip()
            if filename == "":
                filename = "results_output.txt"
            save_results_to_file(student_names, student_results, filename)
        elif choice == "6":
            print("\nThank you for using the Grade Calculator!")
            break
        else:
            print("Invalid choice! Please select 1-6.")


if __name__ == "__main__":
    main_menu()
