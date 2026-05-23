import csv

students = []

# Function to calculate grade


def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


# Save student data in the csv file


def save_students():
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow(["Name", "Roll Number", "Marks", "Grade"])

        for student in students:
            writer.writerow(
                [
                    student["name"],
                    student["roll_number"],
                    student["marks"],
                    student["grade"],
                ]
            )


# Load existing student data


def load_students():
    with open("students.csv", "r") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            student = {
                "name": row[0],
                "roll_number": row[1],
                "marks": float(row[2]),
                "grade": row[3],
            }

            students.append(student)


load_students()


while True:
    print("\n========= STUDENT MANAGEMENT SYSTEM =========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        roll_number = input("Enter Roll Number: ")
        marks = float(input("Enter Marks: "))

        grade = calculate_grade(marks)

        student = {
            "name": name,
            "roll_number": roll_number,
            "marks": marks,
            "grade": grade,
        }

        students.append(student)

        save_students()

        print("Student Added Successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No Students Found!")
        else:
            print("\n ======= Student Records =======")

            for student in students:
                print(f"Name         :  {student['name']}")
                print(f"Roll Number  :  {student['roll_number']}")
                print(f"Marks        :  {student['marks']}")
                print(f"Grade        :  {student['grade']}")
                print("---------------------------------")

    elif choice == "3":
        roll_number = input("Enter Roll Number for Search: ")

        found = False

        for student in students:
            if student["roll_number"] == roll_number:
                print("\nStudent Found!")
                print(f"Name         :  {student['name']}")
                print(f"Roll Number  :  {student['roll_number']}")
                print(f"Marks        :  {student['marks']}")
                print(f"Grade        :  {student['grade']}")

                found = True
                break

        if not found:
            print("Student Not Found!")

    elif choice == "4":
        roll_number = input("Enter Roll Number to Update Marks: ")

        found = False

        for student in students:
            if student["roll_number"] == roll_number:
                new_marks = float(input("Enter new marks: "))

                student["marks"] = new_marks
                student["grade"] = calculate_grade(new_marks)

                save_students()

                print("Record Updated Successfully!")

                found = True
                break

        if not found:
            print("Student Not Found!")

    elif choice == "5":
        roll_number = input("Enter Roll Number to Delete: ")

        found = False

        for student in students:
            if student["roll_number"] == roll_number:
                students.remove(student)

                save_students()

                print("Student Deleted Successfully")

                found = True
                break

        if not found:
            print("Student Not Found!")

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid Choice!")
