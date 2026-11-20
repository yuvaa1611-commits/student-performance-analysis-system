import csv

students = []

subjects = ["Python", "Maths", "Physics", "Digital Logic", "English"]


def get_marks(subject):
    while True:
        try:
            marks = float(input("Enter marks in " + subject + ": "))

            if marks >= 0 and marks <= 100:
                return marks
            else:
                print("Marks should be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


def calculate_percentage(marks):
    total = sum(marks)
    percentage = total / len(marks)
    return total, percentage


def get_grade(percentage):
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


def add_student():
    print("\n--- Add Student ---")

    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")

    marks = []

    for subject in subjects:
        marks.append(get_marks(subject))

    total, percentage = calculate_percentage(marks)
    grade = get_grade(percentage)

    student = {
        "id": student_id,
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }

    students.append(student)

    print("\nStudent added successfully!")
    print("Name:", name)
    print("Total:", total)
    print("Percentage:", round(percentage, 2))
    print("Grade:", grade)


def view_students():
    print("\n--- All Students ---")

    if len(students) == 0:
        print("No students available.")
        return

    for student in students:
        print("\nID:", student["id"])
        print("Name:", student["name"])
        print("Total:", student["total"])
        print("Percentage:", round(student["percentage"], 2))
        print("Grade:", student["grade"])


def search_student():
    print("\n--- Search Student ---")

    student_id = input("Enter student ID: ")

    for student in students:
        if student["id"] == student_id:
            print("\nStudent Found")
            print("ID:", student["id"])
            print("Name:", student["name"])

            for i in range(len(subjects)):
                print(subjects[i] + ":", student["marks"][i])

            print("Total:", student["total"])
            print("Percentage:", round(student["percentage"], 2))
            print("Grade:", student["grade"])
            return

    print("Student not found.")


def find_highest():
    print("\n--- Highest Performer ---")

    if len(students) == 0:
        print("No students available.")
        return

    highest = students[0]

    for student in students:
        if student["percentage"] > highest["percentage"]:
            highest = student

    print("Name:", highest["name"])
    print("Percentage:", round(highest["percentage"], 2))
    print("Grade:", highest["grade"])


def find_lowest():
    print("\n--- Lowest Performer ---")

    if len(students) == 0:
        print("No students available.")
        return

    lowest = students[0]

    for student in students:
        if student["percentage"] < lowest["percentage"]:
            lowest = student

    print("Name:", lowest["name"])
    print("Percentage:", round(lowest["percentage"], 2))
    print("Grade:", lowest["grade"])


def subject_analysis():
    print("\n--- Subject Analysis ---")

    if len(students) == 0:
        print("No students available.")
        return

    for i in range(len(subjects)):
        total = 0

        for student in students:
            total = total + student["marks"][i]

        average = total / len(students)

        print(subjects[i], "average:", round(average, 2))


def save_data():
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(
            ["ID", "Name", "Python", "Maths", "Physics",
             "Digital Logic", "English", "Total",
             "Percentage", "Grade"]
        )

        for student in students:
            writer.writerow(
                [student["id"],
                 student["name"],
                 student["marks"][0],
                 student["marks"][1],
                 student["marks"][2],
                 student["marks"][3],
                 student["marks"][4],
                 student["total"],
                 student["percentage"],
                 student["grade"]]
            )

    print("Data saved successfully.")


def load_data():
    try:
        with open("students.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                marks = [
                    float(row["Python"]),
                    float(row["Maths"]),
                    float(row["Physics"]),
                    float(row["Digital Logic"]),
                    float(row["English"])
                ]

                student = {
                    "id": row["ID"],
                    "name": row["Name"],
                    "marks": marks,
                    "total": float(row["Total"]),
                    "percentage": float(row["Percentage"]),
                    "grade": row["Grade"]
                }

                students.append(student)

    except FileNotFoundError:
        pass


def main():
    load_data()

    while True:
        print("\n================================")
        print(" STUDENT PERFORMANCE ANALYSIS")
        print("================================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Find Highest Performer")
        print("5. Find Lowest Performer")
        print("6. Subject Analysis")
        print("7. Save Data")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            find_highest()

        elif choice == "5":
            find_lowest()

        elif choice == "6":
            subject_analysis()

        elif choice == "7":
            save_data()

        elif choice == "8":
            save_data()
            print("Thank you for using the program.")
            break

        else:
            print("Invalid choice. Please try again.")


main()